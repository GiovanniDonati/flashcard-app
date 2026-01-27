from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from config.security import create_access_token, verify_password
from domain.User import User


def create_token_for_user(session: Session, email: str, password: str):
    user = session.scalar(select(User).where(User.email == email))

    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Incorrect user or password",
        )

    access_token = create_access_token(data={"sub": user.username})
    return access_token


def refresh_token(username: str):
    new_access_token = create_access_token(data={"sub": username})
    return new_access_token
