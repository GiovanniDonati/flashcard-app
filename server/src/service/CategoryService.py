from fastapi import HTTPException
from http import HTTPStatus
from sqlalchemy import select

from domain.Category import Category


def get_all_categories_service(session, category, limit, skip):
    query = select(Category)
    if category:
        query = query.where(Category.name == category)
    query = query.offset(skip).limit(limit)
    categories = session.execute(query).scalars().all()

    return {"categories": categories}


def get_category_service(category_id, session):
    db_category = session.get(Category, category_id)

    if not db_category:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Category not found",
        )

    return db_category


def create_category_service(category, session):
    db_category = session.scalar(
        select(Category).where(Category.name == category.name)
    )

    if db_category:
        if db_category.name == category.name:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Category already exists",
            )

    db_category = Category(
        name=category.name,
    )
    session.add(db_category)
    session.commit()
    session.refresh(db_category)

    return db_category


def update_category_service(category_id, category, session):
    db_category = session.get(Category, category_id)

    if not db_category:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="Category not found",
        )

    for key, value in category.model_dump(exclude_unset=True).items():
        setattr(db_category, key, value)

    session.commit()

    return {"message": "category updated successfully"}


def delete_category_service(category_id, session):
    db_category = session.get(Category, category_id)

    if not db_category:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="category not found",
        )

    session.delete(db_category)
    session.commit()

    return {"message": "category deleted successfully"}
