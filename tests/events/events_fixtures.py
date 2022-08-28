import pytest


@pytest.fixture
def mock_register_body():
    data = {
        "name": "Primer evento",
        "room": 2,
        "event_date": "2022-08-28",
        "created_by": 1
    }
    return data


@pytest.fixture
def mock_register_response():
    data = {
        "status": 201,
        "success": True,
        "msg": "Event created!",
        "data": {
            "id": 1,
            "name": "Primer evento",
            "room": 2,
            "private": False,
            "event_date": "2022-08-28",
            "available": True,
            "created_by": 1,
            "created_at": "2022-08-28T18:23:20.162062Z",
            "updated_at": "2022-08-28T18:23:20.162073Z"
        }
    }
    return data


@pytest.fixture
def mock_get_public_events():
    data = {
    "status": 200,
    "success": True,
    "msg": "List of events",
    "data": [
            {
            "id": 1,
            "name": "Primer evento",
            "room": 2,
            "private": False,
            "event_date": "2022-08-28",
            "available": True,
            "created_by": 1,
            "created_at": "2022-08-27T01:37:31.681764Z",
            "updated_at": "2022-08-27T01:37:31.681785Z"
            }
        ]
    }
    return data


@pytest.fixture
def mock_delete_event():
    data = {
        "status": 204,
        "success": True,
        "msg": "Event was deleted"
    }
    return data


@pytest.fixture
def mock_disable_event():
    data = {
        "status": 200,
        "success": True,
        "msg": "Event disabled",
        "data": {
            "id": 1,
            "name": "Primer evento",
            "room": 2,
            "private": False,
            "event_date": "2022-08-28",
            "available": False,
            "created_by": 1,
            "created_at": "2022-08-28T18:19:58.087867Z",
            "updated_at": "2022-08-28T19:08:31.443285Z"
        }
    }
    return data
