from http import HTTPStatus
from fastapi import FastAPI

from schema.UtilSchema import Message
from controller import CategoryController, UserController, AuthController

router = FastAPI()

router.include_router(UserController.router)
router.include_router(AuthController.router)
router.include_router(CategoryController.router)


@router.get(
    "/",
    status_code=HTTPStatus.OK,
    response_model=Message,
    tags=["Health Check"],
)
def health_check():
    return {"message": "Server running"}
