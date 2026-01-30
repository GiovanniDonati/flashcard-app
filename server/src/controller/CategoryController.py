from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, Depends
from pytest import Session

from config.database import get_session
from schema.CategorySchema import (
    CategoryList,
    CategoryRequest,
    CategoryUpdate,
    CategoryPublic,
)
from service.CategoryService import (
    get_all_categories_service,
    get_category_service,
    create_category_service,
    update_category_service,
    delete_category_service,
)


router = APIRouter(prefix="/categories", tags=["Categories"])
T_Session = Annotated[Session, Depends(get_session)]


@router.get("/", status_code=HTTPStatus.OK, response_model=CategoryList)
def get_categories(
    session: T_Session,
    name: str | None = None,
    limit: int = 10,
    skip: int = 0,
):
    return get_all_categories_service(session, name, limit, skip)


@router.get("/{category_id}", status_code=HTTPStatus.OK)
def get_category(category_id: int, session: T_Session):
    return get_category_service(category_id, session)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=CategoryPublic)
def create_category(category: CategoryRequest, session: T_Session):
    return create_category_service(category, session)


@router.patch("/{category_id}", status_code=HTTPStatus.OK)
def update_category(
    category_id: int, category: CategoryUpdate, session: T_Session
):
    return update_category_service(category_id, category, session)


@router.delete("/{category_id}", status_code=HTTPStatus.OK)
def delete_category(category_id: int, session: T_Session):
    return delete_category_service(category_id, session)
