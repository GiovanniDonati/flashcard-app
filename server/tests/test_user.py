from http import HTTPStatus
from schema.UserSchema import UserPublic


def test_create_user_return_created(client):
    response = client.post(
        "/users/",
        json={
            "name": "Giovanni",
            "username": "donati_dev",
            "email": "donati_dev@dev.com",
            "password": "securepassword",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "Giovanni",
        "username": "donati_dev",
        "email": "donati_dev@dev.com",
    }


def test_get_user_return_ok_and_user_list(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"users": []}


def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get("/users/")
    assert response.json() == {"users": [user_schema]}


def test_update_user_return_ok(client, user):
    response = client.patch(f"/users/{user.id}", json={"username": "tested"})
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "user updated successfully"}


def test_delete_user_return_ok_and_success_message(client, user):
    response = client.delete(f"/users/{user.id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "user deleted successfully"}
