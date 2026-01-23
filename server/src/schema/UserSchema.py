from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserRequest(BaseModel):
    user: str
    email: EmailStr
    password: str


class UserSchema(UserRequest):
    id: UUID


class UserPublic(BaseModel):
    username: str
    email: EmailStr
