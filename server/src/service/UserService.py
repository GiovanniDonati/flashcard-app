from fastapi import HTTPException
from http import HTTPStatus
from sqlalchemy import select

from domain.User import User


def get_users_service(session, user, limit, skip):
    query = select(User)
    if user:
        query = query.where(User.username == user)
    query = query.offset(skip).limit(limit)
    users = session.execute(query).scalars().all()

    return {"users": users}


def get_user_service(user_id, session):
    db_user = session.get(User, user_id)

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )

    return db_user


def create_user_service(user, session):
    db_user = session.scalar(
        select(User).where(
            (User.username == user.username) | (User.email == user.email)
        )
    )

    if db_user:
        if db_user.username == user.username:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Username already exists",
            )
        elif db_user.email == user.email:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Email already exists",
            )

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def update_user_service(user_id, user, session):
    db_user = session.get(User, user_id)

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )

    if user.username:
        db_user.username = user.username
    if user.email:
        db_user.email = user.email
    if user.password:
        db_user.password = user.password

    session.commit()

    return {"message": "user updated successfully"}


def delete_user_service(user_id, session):
    db_user = session.get(User, user_id)

    if not db_user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )

    session.delete(db_user)
    session.commit()

    return {"message": "user deleted successfully"}
