from pydantic import BaseModel, ConfigDict


class CategoryRequest(BaseModel):
    name: str


class CategoryPublic(CategoryRequest):
    id: int
    model_config = ConfigDict(from_attributes=True)


class CategoryUpdate(BaseModel):
    name: str | None = None


class CategoryList(BaseModel):
    categories: list[CategoryPublic]
