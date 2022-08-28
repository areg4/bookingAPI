import pytest


@pytest.fixture
def mock_register_body():
    data = {
        "customer": 1,
        "event": 2
    }
    return data


@pytest.fixture
def mock_register_reponse():
    data = {
        "status": 201,
        "success": True,
        "msg": "Book created!",
        "data": {
            "id": 4,
            "customer": 1,
            "event": 2,
            "available": True,
            "created_at": "2022-08-28T18:44:22.469277Z",
            "updated_at": "2022-08-28T18:44:22.469291Z"
        }
    }
    return data


@pytest.fixture
def mock_get_all_books():
    data = {
        "status": 200,
        "success": True,
        "msg": "List of books",
        "data": [
            {
            "id": 4,
            "customer": 1,
            "event": 2,
            "available": True,
            "created_at": "2022-08-28T18:44:22.469277Z",
            "updated_at": "2022-08-28T18:44:22.469291Z"
            }
        ]
    }
    return data


@pytest.fixture
def mock_get_books_by_cutomer():
    data = {
        "status": 200,
        "success": True,
        "msg": "List of books by customer",
        "data": [
                    {
                    "id": 1,
                    "customer": 1,
                    "event": 2,
                    "available": True,
                    "created_at": "2022-08-28T18:44:22.469277Z",
                    "updated_at": "2022-08-28T18:44:22.469291Z"
                    }
                ]
    }
    return data


@pytest.fixture
def mock_cancel_book():
    data = {
        "status": 200,
        "success": True,
        "msg": "Book canceled",
        "data": {
            "id": 4,
            "customer": 1,
            "event": 2,
            "available": False,
            "created_at": "2022-08-28T18:44:22.469277Z",
            "updated_at": "2022-08-28T18:48:23.268816Z"
        }
    }
    return data
