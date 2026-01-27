from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config.security import get_current_user
from config.database import get_session
from domain.User import User
from schema.UtilSchema import Token
from service import AuthService

router = APIRouter(prefix="/auth", tags=["Authentication"])

T_Session = Annotated[Session, Depends(get_session)]
T_OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]


@router.post("/token", response_model=Token)
def login_for_access_token(session: T_Session, form_data: T_OAuth2Form):
    access_token = AuthService.create_token_for_user(
        session, form_data.username, form_data.password
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/refresh_token", response_model=Token)
def refresh_access_token(
    user: User = Depends(get_current_user),
):
    new_access_token = AuthService.refresh_token(user.username)
    return {"access_token": new_access_token, "token_type": "bearer"}
