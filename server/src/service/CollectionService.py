from fastapi import HTTPException
from http import HTTPStatus
from sqlalchemy import select

from domain.Collection import Collection


def get_all_collections_service(session, collection, limit, skip):
    query = select(Collection)
    if collection:
        query = query.where(Collection.name == collection)
    query = query.offset(skip).limit(limit)
    collections = session.execute(query).scalars().all()

    return {"collections": collections}


def get_collection_service(collection_id, session):
    db_collection = session.get(Collection, collection_id)

    if not db_collection:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Collection not found",
        )

    return db_collection


def create_collection_service(collection, session):
    db_collection = session.scalar(
        select(Collection).where(Collection.name == collection.name)
    )

    if db_collection:
        if db_collection.name == collection.name:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Collection already exists",
            )

    db_collection = Collection(
        name=collection.name,
    )
    session.add(db_collection)
    session.commit()
    session.refresh(db_collection)

    return db_collection


def update_collection_service(collection_id, collection, session):
    db_collection = session.get(Collection, collection_id)

    if not db_collection:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Collection not found",
        )

    for key, value in collection.model_dump(exclude_unset=True).items():
        setattr(db_collection, key, value)

    session.commit()

    return {"message": "collection updated successfully"}


def delete_collection_service(collection_id, session):
    db_collection = session.get(Collection, collection_id)

    if not db_collection:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="collection not found",
        )

    session.delete(db_collection)
    session.commit()

    return {"message": "collection deleted successfully"}
