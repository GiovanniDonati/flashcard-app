import pytest
from http import HTTPStatus
from fastapi.testclient import TestClient

from src.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_return_ok_and_server_started(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Server started"}


def test_get_user_return_ok_and_user_list(client):
    response = client.get("/user/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [{"username": "donati_dev", "email": "donati@dev.com"}]
    }


def test_create_user_return_created(client):
    response = client.post(
        "/user/",
        json={
            "username": "donati_dev",
            "email": "donati@dev.com",
            "password": "securepassword",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {"username": "donati_dev", "email": "donati@dev.com"}


def test_update_user_return_ok_and_updated_user(client):
    response = client.patch("/user/1", json={"username": "updated_test"})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "user updated successfully"}


def test_delete_user_return_ok_and_success_message(client):
    response = client.delete("/user/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "user deleted successfully"}
