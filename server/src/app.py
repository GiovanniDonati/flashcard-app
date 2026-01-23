from http import HTTPStatus
from fastapi import FastAPI

from .schema.UserSchema import UserPublic, UserRequest

app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Server started'}


@app.post('/user/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserRequest):
    return user


@app.patch('/user/{id}')
def update_user(id: int, user: UserRequest):
    return user


@app.delete('/user/{id}')
def delete_user(id: int):
    return {'message':'user deleted successfully'}
