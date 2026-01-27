from http import HTTPStatus
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_session
from config.security import create_access_token, verify_password
from schema.UserSchema import UserList, UserPublic, UserRequest, UserUpdate
from schema.UtilSchema import Token
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
    return get_all_users_service(session, user, limit, skip)


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


@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    if not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}
