import datetime
import os
import time

import pytest
import requests

def pytest_addoption(parser):
    parser.addoption('--url', help='Tator host url', default='https://adamant.duckdns.org')
    parser.addoption('--token', help='API token', default='')

def pytest_generate_tests(metafunc):
    if 'url' in metafunc.fixturenames:
          metafunc.parametrize('url', [metafunc.config.getoption('url')])
    if 'token' in metafunc.fixturenames:
          metafunc.parametrize('token', [metafunc.config.getoption('token')])

def make_attribute_types():
    return [
        dict(
            name='test_bool',
            dtype='bool',
            default=True,
        ),
        dict(
            name='test_int',
            dtype='int',
            default=0,
            minimum=-1000,
            maximum=1000,
        ),
        dict(
            name='test_float',
            dtype='float',
            default=0.0,
            minimum=-1000.0,
            maximum=1000.0,
        ),
        dict(
            name='test_enum',
            dtype='enum',
            choices=['a', 'b', 'c'],
            default='a',
        ),
        dict(
            name='test_string',
            dtype='string',
            default='asdf',
        ),
        dict(
            name='test_datetime',
            dtype='datetime',
            use_current=True,
        ),
        dict(
            name='test_geopos',
            dtype='geopos',
            default=[-179.0, -89.0],
        ),
    ]

@pytest.fixture(scope='session')
def project(request):
    """ Project ID for a created project. """
    import tator
    url = request.config.option.url
    token = request.config.option.token
    tator_api = tator.get_api(url, token)
    current_dt = datetime.datetime.now()
    dt_str = current_dt.strftime('%Y_%m_%d__%H_%M_%S')
    response = tator_api.create_project(project_spec={
        'name': f'test_project_{dt_str}',
        'summary': f'Test project created by pytator unit tests on {current_dt}',
    })
    project_id = response.id
    yield project_id
    status = tator_api.delete_project(project_id)

@pytest.fixture(scope='session')
def video_type(request, project):
    import tator
    url = request.config.option.url
    token = request.config.option.token
    tator_api = tator.get_api(url, token)
    response = tator_api.create_media_type(project, media_type_spec={
        'name': 'video_type',
        'description': 'Test video type',
        'project': project,
        'dtype': 'video',
    })
    video_type_id = response.id
    yield video_type_id
    response = tator_api.delete_media_type(video_type_id)

@pytest.fixture(scope='session')
def video(request, project, video_type):
    import tator
    from tator.util import upload_media
    url = request.config.option.url
    token = request.config.option.token
    tator_api = tator.get_api(url, token)
    out_path = '/tmp/ForBiggerEscapes.mp4'
    if not os.path.exists(out_path):
        url = 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4'
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(out_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
    response = upload_media(out_path, video_type, tator_api)
    print(response.message)
    while True:
        response = tator_api.get_media_list(project, name='ForBiggerEscapes.mp4')
        if len(response) > 0:
            video_id = response[0].id
            break
        print("Waiting for transcode...")
        time.sleep(2.5)
    yield video_id
    response = tator_api.delete_media(video_id)

@pytest.fixture(scope='session')
def box_type(request, project, video_type):
    import tator
    url = request.config.option.url
    token = request.config.option.token
    tator_api = tator.get_api(url, token)
    response = tator_api.create_localization_type(project, localization_type_spec={
        'name': 'box_type',
        'description': 'Test box type',
        'project': project,
        'media_types': [video_type],
        'dtype': 'box',
        'attribute_types': make_attribute_types(),
    })
    box_type_id = response.id
    yield box_type_id
    response = tator_api.delete_localization_type(box_type_id)

@pytest.fixture(scope='session')
def state_type(request, project, video_type):
    import tator
    url = request.config.option.url
    token = request.config.option.token
    tator_api = tator.get_api(url, token)
    response = tator_api.create_state_type(project, state_type_spec={
        'name': 'state_type',
        'description': 'Test state type',
        'project': project,
        'media_types': [video_type],
        'association': 'Frame',
        'attribute_types': make_attribute_types(),
    })
    state_type_id = response.id
    yield state_type_id
    response = tator_api.delete_state_type(state_type_id)

@pytest.fixture(scope='session')
def track_type(request, project, video_type):
    import tator
    url = request.config.option.url
    token = request.config.option.token
    tator_api = tator.get_api(url, token)
    response = tator_api.create_state_type(project, state_type_spec={
        'name': 'track_type',
        'description': 'Test track type',
        'project': project,
        'media_types': [video_type],
        'association': 'Localization',
        'attribute_types': make_attribute_types(),
    })
    state_type_id = response.id
    yield state_type_id
    response = tator_api.delete_state_type(state_type_id)
