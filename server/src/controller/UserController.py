from http import HTTPStatus
from typing_extensions import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_session
from schema.UserSchema import UserList, UserPublic, UserRequest, UserUpdate
from service.UserService import *

router = APIRouter(prefix="/users", tags=["Users"])
T_Session = Annotated[Session, Depends(get_session)]


@router.get("/", status_code=HTTPStatus.OK, response_model=UserList)
def get_users(
    session: T_Session,
    user: str | None = None,
    limit: int = 10,
    skip: int = 0,
):
    return get_users_service(session, user, limit, skip)


@router.get("/{user_id}", status_code=HTTPStatus.OK, response_model=UserPublic)
def get_user(user_id: int, session: T_Session):
    return get_user_service(user_id, session)


@router.post("/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserRequest, session: T_Session):
    return create_user_service(user, session)


@router.patch("/{user_id}", status_code=HTTPStatus.OK)
def update_user(user_id: int, user: UserUpdate, session: T_Session):
    return update_user_service(user_id, user, session)


@router.delete("/{user_id}", status_code=HTTPStatus.OK)
def delete_user(user_id: int, session: T_Session):
    return delete_user_service(user_id, session)
