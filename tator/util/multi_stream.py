import math
import os
import requests
import subprocess
import tempfile
import logging
from uuid import uuid1

from ._upload_file import _upload_file
import tator

logger = logging.getLogger(__name__)

def _download_file(headers, url, out_path):
    CHUNK_SIZE=2*1024*1024
    with requests.get(url, stream=True, headers=headers) as r:
        r.raise_for_status()
        total_size = r.headers['Content-Length']
        total_chunks = math.ceil(int(total_size) / CHUNK_SIZE)
        chunk_count = 0
        last_progress = 0
        with open(out_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    chunk_count += 1
                    f.write(chunk)

def make_multi_stream(api, type_id, layout, name, media_ids, section, quality=None):
    """ Uploads a single media file.

    :param api: :class:`tator.TatorApi` object.
    :param type_id: Unique integer identifying a multi-stream media type.
    :param layout: 2 element list of integers defining layout as [rows, cols].
    :param name: Name of the file to use
    :param media_ids: List of media_ids to multi-stream
    :param section: Section name. If this section does not exist it will be created.
    :param quality: [Optional] Media section to upload to.
    :returns: Response from media object creation.
    """

    # Fetch the stuff we need to download files
    config = api.api_client.configuration
    host = config.host
    token = config.api_key['Authorization']
    prefix = config.api_key_prefix['Authorization']

    # use a multi extension
    name += ".multi"

    # Fetch the media type
    multi_stream_type = api.get_media_type(type_id)
    project = multi_stream_type.project
   
    # Fetch the section. If it does not exist, create it. 
    sections = api.get_section_list(project, name=section)
    if len(sections) == 0:
        section_spec = {'name': section, 'tator_user_sections': str(uuid1())}
        response = api.create_section(project, section_spec=section_spec)
        section_obj = api.get_section_list(project, name=section)[0]
    else:
        section_obj = sections[0]

    assert(len(media_ids) == layout[0]*layout[1])

    media_objects = api.get_media_list(project, media_id=media_ids)
    assert(len(media_objects) == len(media_ids))

    media_lookup={}
    for media in media_objects:
        media_lookup[media.id] = media

    attributes={}
    if section:
        attributes.update({"tator_user_sections": section_obj.tator_user_sections})

    headers = {
        'Authorization': f'{prefix} {token}',
        'Content-Type': f'application/json',
        'Accept-Encoding': 'gzip',
    }

    # Download the thumbnails into a temporary
    with tempfile.TemporaryDirectory() as d:
        for pos,media_id in enumerate(media_ids):
            media = media_lookup[media_id]
            thumb = host + "/media/" + media.thumbnail
            thumb_gif = host + "/media/" + media.thumbnail_gif
            _download_file(headers, thumb, os.path.join(d,
                                                        f"thumb_{pos:09d}.jpg"))
            _download_file(headers, thumb_gif, os.path.join(d,
                                                        f"gif_{pos:09d}.gif"))

        cmd = ["ffmpeg",
               "-y",
               "-i", "thumb_%09d.jpg",
               "-vf",f"tile={layout[1]}x{layout[0]},scale=256:-1",
               os.path.join(d,"tiled_thumb.jpg")]
        subprocess.run(cmd,cwd=d,check=True)

        input_files=[]
        rows=layout[0]
        cols=layout[1]
        filter_graph=""
        idx = 0
        for row in range(rows):
            for col in range(cols):
                filter_graph += f"[{idx}:v]"
                idx+=1
                if cols > 1 and col + 1 == cols:
                    filter_graph += f"hstack=inputs={cols}[r{row}];"
        for row in range(rows):
            if cols > 1:
                filter_graph += f"[r{row}]"
        if rows > 1 and row + 1 == rows:
            filter_graph+=f'vstack=inputs={rows}[tiled_gif];[tiled_gif]'
        filter_graph+=f'scale=256:-1[raw];[raw]split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse[final]'
        print(filter_graph)
        for pos,_ in enumerate(media_ids):
            input_files.extend(['-i', f'gif_{pos:09d}.gif'])
        cmd = ["ffmpeg",
               "-y",
               *input_files,
               "-filter_complex", filter_graph,
               "-map", "[final]",
               "-shortest",
               "tiled_gif.gif"]

        subprocess.run(cmd, cwd=d, check=True)

        md5=tator.util.md5sum(os.path.join(d,'tiled_gif.gif'))

        media_spec = {'attributes': attributes,
                      'name': name,
                      'md5': md5,
                      'section': section_obj.name,
                      'type': type_id}

        resp = api.create_media(project, media_spec)
        print(f"Created {resp.id}")

        for progress, thumbnail_info in _upload_file(api, project, os.path.join(d,'tiled_thumb.jpg')):
            logger.info(f"Thumbnail upload progress: {progress}%")
        for progress, thumbnail_gif_info in _upload_file(api, project, os.path.join(d,'tiled_gif.gif')):
            logger.info(f"Thumbnail gif upload progress: {progress}%")
        download_info = api.get_download_info(project, {'keys': [thumbnail_info.key,
                                                                 thumbnail_gif_info.key]})
        download_info = {info.key:info.url for info in download_info}

        media_files={"layout": layout,
                     "ids": media_ids}
        if quality:
            media_files.update({"quality": quality})
        api.update_media(resp.id,
                         {"thumbnail_gif_url": download_info[thumbnail_gif_info.key],
                          "thumbnail_url": download_info[thumbnail_info.key],
                          "media_files": media_files})
        return resp

