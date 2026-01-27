from http import HTTPStatus


def test_root_return_ok_and_server_started(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Server running"}


def test_get_token(client, user):
    response = client.post(
        "/auth/token",
        data={"username": user.email, "password": user.clean_password},
    )
    token = response.json()

    assert response.status_code == HTTPStatus.OK
    assert "access_token" in token
    assert "token_type" in token
