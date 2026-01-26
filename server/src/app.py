from http import HTTPStatus
from fastapi import FastAPI

from schema.UtilsSchema import Message
from controller import UserController

router = FastAPI()

router.include_router(UserController.router)


@router.get(
    "/",
    status_code=HTTPStatus.OK,
    response_model=Message,
    tags=["Health Check"],
)
def health_check():
    return {"message": "Server running"}
