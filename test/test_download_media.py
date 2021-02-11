import os
import tempfile

import tator

def test_download_video(host, token, video):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    archival = video_obj.media_files.archival
    streaming = video_obj.media_files.streaming

    available = [x.resolution[0] for x in archival]
    best = max(available)
    best_idx = available.index(best)

    # Verify we get the best archival when we ask
    with tempfile.TemporaryDirectory() as td:
        video_path = os.path.join(td, video_obj.name)
        for progress in tator.download_media(
                tator_api,
                video_obj,
                video_path,
                quality=None,
                media_type=None):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(video_path)
        assert os.stat(video_path).st_size == archival[best_idx].size

    for idx,video_file in enumerate(archival):
        with tempfile.TemporaryDirectory() as td:
            video_path = os.path.join(td, video_obj.name)
            for progress in tator.download_media(
                    tator_api,
                    video_obj,
                    video_path,
                    quality=video_file.resolution[0],
                    media_type='archival'):
                print(f"Media download progress: {progress}%")
            assert os.path.exists(video_path)
            assert os.stat(video_path).st_size == video_file.size



    # Verify we can download the best when we ask (streaming)
    available = [x.resolution[0] for x in streaming]
    best = max(available)
    best_idx = available.index(best)

    # Verify we get the best streaming when we ask
    with tempfile.TemporaryDirectory() as td:
        video_path = os.path.join(td, video_obj.name)
        for progress in tator.download_media(
                tator_api,
                video_obj,
                video_path,
                quality=None,
                media_type='streaming'):
            print(f"Media download progress: {progress}%")
        assert os.path.exists(video_path)
        assert os.stat(video_path).st_size == streaming[best_idx].size


    # Verify we can download each file size
    for video_file in streaming:
        with tempfile.TemporaryDirectory() as td:
            video_path = os.path.join(td, video_obj.name)
            for progress in tator.download_media(
                    tator_api,
                    video_obj,
                    video_path,
                    quality=video_file.resolution[0],
                    media_type='streaming'):
                print(f"Media download progress: {progress}%")
            assert os.path.exists(video_path)
            assert os.stat(video_path).st_size == video_file.size
