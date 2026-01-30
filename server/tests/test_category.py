from http import HTTPStatus
from schema.CategorySchema import CategoryPublic


def test_create_category_return_created(client):
    response = client.post(
        "/categories/",
        json={
            "name": "Test Category",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "name": "Test Category",
        "id": 1,
    }


def test_get_category_return_ok_and_category_list(client):
    response = client.get("/categories/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"categories": []}


def test_read_categories_with_categories(client, category):
    category_schema = CategoryPublic.model_validate(category).model_dump()
    response = client.get("/categories/")
    assert response.json() == {"categories": [category_schema]}


def test_update_category_return_ok(client, category):
    response = client.patch(
        f"/categories/{category.id}", json={"name": "tested"}
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "category updated successfully"}


def test_delete_category_return_ok_and_success_message(client, category):
    response = client.delete(f"/categories/{category.id}")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "category deleted successfully"}
