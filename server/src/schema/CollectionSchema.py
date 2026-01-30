from pydantic import BaseModel, ConfigDict


class CollectionRequest(BaseModel):
    name: str


class CollectionPublic(CollectionRequest):
    id: int
    model_config = ConfigDict(from_attributes=True)


class CollectionUpdate(BaseModel):
    name: str | None = None


class CollectionList(BaseModel):
    collections: list[CollectionPublic]
