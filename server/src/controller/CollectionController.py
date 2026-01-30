from http import HTTPStatus
from typing import Annotated
from fastapi import APIRouter, Depends
from pytest import Session

from config.database import get_session
from schema.CollectionSchema import (
    CollectionList,
    CollectionRequest,
    CollectionUpdate,
    CollectionPublic,
)
from service.CollectionService import (
    get_all_collections_service,
    get_collection_service,
    create_collection_service,
    update_collection_service,
    delete_collection_service,
)


router = APIRouter(prefix="/collection", tags=["Collections"])
T_Session = Annotated[Session, Depends(get_session)]


@router.get("/", status_code=HTTPStatus.OK, response_model=CollectionList)
def get_collections(
    session: T_Session,
    name: str | None = None,
    limit: int = 10,
    skip: int = 0,
):
    return get_all_collections_service(session, name, limit, skip)


@router.get("/{collection_id}", status_code=HTTPStatus.OK)
def get_collection(collection_id: int, session: T_Session):
    return get_collection_service(collection_id, session)


@router.post(
    "/", status_code=HTTPStatus.CREATED, response_model=CollectionPublic
)
def create_collection(collection: CollectionRequest, session: T_Session):
    return create_collection_service(collection, session)


@router.patch("/{collection_id}", status_code=HTTPStatus.OK)
def update_collection(
    collection_id: int, collection: CollectionUpdate, session: T_Session
):
    return update_collection_service(collection_id, collection, session)


@router.delete("/{collection_id}", status_code=HTTPStatus.OK)
def delete_collection(collection_id: int, session: T_Session):
    return delete_collection_service(collection_id, session)
