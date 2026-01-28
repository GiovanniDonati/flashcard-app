import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session

from config.database import get_session
from config.security import get_password_hash
from app import router
from domain.User import User, table_registry


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(router) as client:
        router.dependency_overrides[get_session] = get_session_override
        yield client

    router.dependency_overrides.clear()


@pytest.fixture
def session():
    engine = create_engine(
        "sqlite+pysqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    table_registry.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture
def user(session):
    password = "testtest"
    user = User(
        name="Teste",
        username="Teste",
        email="teste@test.com",
        password=get_password_hash(password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user
