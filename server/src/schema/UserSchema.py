from pydantic import BaseModel, ConfigDict, EmailStr


class UserRequest(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str


class UserSchema(UserRequest):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserPublic(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    name: str | None = None
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class UserList(BaseModel):
    users: list[UserPublic]
