from http import HTTPStatus


def test_root_return_ok_and_server_started(client):
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Server started"}
