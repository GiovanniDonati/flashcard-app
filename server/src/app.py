from http import HTTPStatus
from fastapi import FastAPI

from schema.UserSchema import UserList, UserPublic, UserRequest, UserUpdate
from schema.UtilsSchema import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Server started"}


@app.get("/user/", status_code=HTTPStatus.OK, response_model=UserList)
def get_user():
    return {"users": [{"username": "donati_dev", "email": "donati@dev.com"}]}


@app.post("/user/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserRequest):
    user = UserPublic(username=user.username, email=user.email)
    return user


@app.patch("/user/{id}", status_code=HTTPStatus.OK, response_model=Message)
def update_user(id: int, user: UserUpdate):
    return {"message": "user updated successfully"}


@app.delete("/user/{id}", status_code=HTTPStatus.OK, response_model=Message)
def delete_user(id: int):
    return {"message": "user deleted successfully"}
