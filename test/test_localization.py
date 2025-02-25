from pprint import pformat
import datetime
import random
from time import sleep
import uuid
from collections import Counter

import tator
from ._common import assert_close_enough


def wait_for_parity(tator_api, project, patch, expected_ids):
    attribute_filter = [f"test_string::{patch['attributes']['test_string']}"]
    localization_id_query = {"ids": expected_ids}
    total_timeout = 60.0 # seconds
    wait_time = 2.0 # seconds

    print(f"Using attribute filter:\n{pformat(attribute_filter)}")
    from_psql = tator_api.get_localization_list_by_id(
        project,
        localization_id_query=localization_id_query,
        attribute=attribute_filter,
    )
    count = tator_api.get_localization_count_by_id(
        project,
        localization_id_query=localization_id_query,
        attribute=attribute_filter,
    )
    assert(len(from_psql) == count)
    for idx in range(int(total_timeout / wait_time) + 1):
        from_es = tator_api.get_localization_list_by_id(
            project,
            localization_id_query=localization_id_query,
            attribute=attribute_filter,
            force_es=1,
        )
        count = tator_api.get_localization_count_by_id(
            project,
            localization_id_query=localization_id_query,
            attribute=attribute_filter,
            force_es=1,
        )
        assert(len(from_es) == count)
        if len(from_es) == len(from_psql):
            print(f"Found expected number of results after {idx * wait_time} seconds")
            return True

        sleep(wait_time)

    print(f"Did not find expected number of results after {idx * wait_time} seconds")
    return False

def random_localization(project, box_type, video_obj, post=False):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    w = random.uniform(0.0, 1.0 - x)
    h = random.uniform(0.0, 1.0 - y)
    attributes = {
        'test_bool': random.choice([False, True]),
        'test_int': random.randint(-1000, 1000),
        'test_float': random.uniform(-1000.0, 1000.0),
        'test_enum': random.choice(['a', 'b', 'c']),
        'test_string': str(uuid.uuid1()),
        'test_datetime': datetime.datetime.now().isoformat(),
        'test_geopos': [random.uniform(-180.0, 180.0), random.uniform(-90.0, 90.0)],
        'test_float_array': [random.uniform(-1.0, 1.0) for _ in range(3)],
    }
    out = {
        'x': x,
        'y': y,
        'width': w,
        'height': h,
        'project': project,
        'type': box_type,
        'media_id': video_obj.id,
        'frame': random.randint(0, video_obj.num_frames - 1),
    }
    if post:
        out = {**out, **attributes}
    else:
        out['attributes'] = attributes
    return out

def comparison_query(tator_api, project, box_ids, exclude):
    """ Runs a random query and compares results with ES enabled and disabled.
    """
    bool_value = random.choice([True, False])
    int_lower = random.randint(-1000, 0)
    int_upper = random.randint(0, 1000)
    float_lower = random.uniform(-1000.0, 0.0)
    float_upper = random.uniform(0.0, 1000.0)
    enum_value = random.choice(['a', 'b', 'c'])
    localization_id_query = {"ids": box_ids}
    attribute_filter = [f"test_bool::{'true' if bool_value else 'false'}", f"test_enum::{enum_value}"]
    attribute_lte_filter = [f"test_int::{int_upper}"]
    attribute_gte_filter = [f"test_int::{int_lower}"]
    attribute_lt_filter = [f"test_float::{float_upper}"]
    attribute_gt_filter = [f"test_float::{float_lower}"]
    print("Starting PSQL query...")
    t0 = datetime.datetime.now()
    from_psql = tator_api.get_localization_list_by_id(
        project,
        localization_id_query=localization_id_query,
        attribute=attribute_filter,
        attribute_lte=attribute_lte_filter,
        attribute_gte=attribute_gte_filter,
        attribute_lt=attribute_lt_filter,
        attribute_gt=attribute_gt_filter,
    )
    psql_time = datetime.datetime.now() - t0
    print("Starting ES query...")
    t0 = datetime.datetime.now()
    from_es = tator_api.get_localization_list_by_id(
        project,
        localization_id_query=localization_id_query,
        attribute=attribute_filter,
        attribute_lte=attribute_lte_filter,
        attribute_gte=attribute_gte_filter,
        attribute_lt=attribute_lt_filter,
        attribute_gt=attribute_gt_filter,
        force_es=1,
    )
    es_time = datetime.datetime.now() - t0

    print("Checking PSQL and ES ids...")
    psql_ids = [ele.id for ele in from_psql]
    es_ids = [ele.id for ele in from_es]
    assert(Counter(psql_ids) == Counter(es_ids))

    print("Checking PSQL and ES values...")
    assert len(from_psql) == len(from_es)
    for psql, es in zip(from_psql, from_es):
        assert_close_enough(psql, es, exclude)
        assert(psql.attributes['test_bool'] == bool_value)
        assert(psql.attributes['test_int'] <= int_upper)
        assert(psql.attributes['test_int'] >= int_lower)
        assert(psql.attributes['test_float'] < float_upper)
        assert(psql.attributes['test_float'] > float_lower)
        assert(psql.attributes['test_enum'] == enum_value)
    return psql_time, es_time

def test_localization_crud(host, token, project, video_type, video, box_type):
    tator_api = tator.get_api(host, token)
    video_obj = tator_api.get_media(video)

    # These fields will not be checked for object equivalence after patch.
    exclude = ['project', 'type', 'media_id', 'id', 'meta', 'user', 'ids']

    # Test bulk create.
    num_localizations = random.randint(2000, 10000)
    boxes = [
        random_localization(project, box_type, video_obj, post=True)
        for _ in range(num_localizations)
    ]
    box_ids = []
    for response in tator.util.chunked_create(tator_api.create_localization_list,
                                         project, localization_spec=boxes):
        box_ids += response.id
    assert len(box_ids) == len(boxes)
    print(f"Created {len(box_ids)} boxes!")

    # Verify list is the right length
    response = tator_api.get_localization_list(project,type=box_type)
    assert len(response) == num_localizations

    # Test media retrieval by localization ID.
    response = tator_api.get_media_list_by_id(project, {'localization_ids': box_ids})
    assert len(response) == 1
    assert response[0].id == video
    response = tator_api.get_media_list_by_id(project, {'localization_ids': box_ids}, force_es=1)
    assert len(response) == 1
    assert response[0].id == video

    # Test box retrieval by media ID.
    response = tator_api.get_localization_list_by_id(project, {'media_ids': [video]})
    assert(len(response) == len(box_ids))
    response = tator_api.get_localization_list_by_id(project, {'media_ids': [video]}, force_es=1)
    assert(len(response) == len(box_ids))

    # Test single create.
    box = random_localization(project, box_type, video_obj, post=True)
    response = tator_api.create_localization_list(project, localization_spec=[box])
    assert isinstance(response, tator.models.CreateListResponse)
    box_id = response.id[0]

    # Patch single box.
    patch = random_localization(project, box_type, video_obj)
    response = tator_api.update_localization(box_id, localization_update=patch)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Get single box.
    updated_box = tator_api.get_localization(box_id)
    assert_close_enough(patch, updated_box, exclude)

    # Get box by ID.
    box_by_id = tator_api.get_localization_list_by_id(project, {'ids': [box_id]})
    assert(len(box_by_id) == 1)
    box_by_id = box_by_id[0]
    assert_close_enough(updated_box, box_by_id, exclude)

    # Delete single box.
    response = tator_api.delete_localization(box_id)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    params = {'media_id': [video], 'type': box_type}
    assert(tator_api.get_localization_count(project, **params) == len(boxes))

    # Bulk update box attributes.
    response = tator_api.create_version(
        project,
        version_spec={
            "name": "Test Version",
            "description": "A version for testing",
        },
    )
    new_version = response.id
    bulk_patch = random_localization(project, box_type, video_obj)
    bulk_patch = {"attributes": bulk_patch["attributes"], "version": new_version}
    response = tator_api.update_localization_list(project, **params,
                                                  localization_bulk_update=bulk_patch)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Bulk update specified boxes by ID.
    id_bulk_patch = random_localization(project, box_type, video_obj)
    update_ids = random.choices(box_ids, k=100)
    id_bulk_patch = {
        "attributes": id_bulk_patch["attributes"],
        "ids": update_ids,
        "version": new_version,
    }
    response = tator_api.update_localization_list(project, **params,
                                                  localization_bulk_update=id_bulk_patch)
    assert isinstance(response, tator.models.MessageResponse)
    print(response.message)

    # Verify all boxes have been updated.
    boxes = tator_api.get_localization_list(project, **params)
    dataframe = tator.util.to_dataframe(boxes)
    assert(len(boxes)==len(dataframe))
    for box in boxes:
        if box.id in update_ids:
            assert_close_enough(id_bulk_patch, box, exclude)
        else:
            assert_close_enough(bulk_patch, box, exclude)

    # Do random queries using psql and elasticsearch and compare results.
    assert wait_for_parity(tator_api, project, id_bulk_patch, update_ids)
    es_time = datetime.timedelta(seconds=0)
    psql_time = datetime.timedelta(seconds=0)
    localization_ids = [box.id for box in boxes]
    NUM_QUERIES = 10
    for _ in range(NUM_QUERIES):
        psql, es = comparison_query(tator_api, project, localization_ids, exclude)
        psql_time += psql
        es_time += es
    print(f"Over {NUM_QUERIES} random attribute queries:")
    print(f"  Avg PSQL time: {psql_time / NUM_QUERIES}")
    print(f"  Avg ES time: {es_time / NUM_QUERIES}")

    # Clone boxes to same media.
    version_mapping = {version.id: version.id for version in tator_api.get_version_list(project)}
    generator = tator.util.clone_localization_list(tator_api, {**params, 'project': project},
                                                   project, version_mapping, {video:video},
                                                   {box_type: box_type}, tator_api)
    for num_created, num_total, response, id_map in generator:
        print(f"Created {num_created} of {num_total} localizations...")
    print(f"Finished creating {num_created} localizations!")
    assert(tator_api.get_localization_count(project, **params) == 2 * len(boxes))

    # Delete all boxes.
    response = tator_api.delete_localization_list(project, **params)
    assert isinstance(response, tator.models.MessageResponse)

    # Verify all boxes are gone.
    boxes = tator_api.get_localization_list(project, **params)
    assert boxes == []

    # Clean up test version
    tator_api.delete_version(new_version)
