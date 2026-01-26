from pydantic import BaseModel, ConfigDict, EmailStr
from uuid import UUID


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserSchema(UserRequest):
    id: UUID


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserList(BaseModel):
    users: list[UserPublic]
