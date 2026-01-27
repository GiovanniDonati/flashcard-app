from sqlalchemy import select

from domain.User import User


def test_create_user(session):
    new_user = User(username="donati", password="secret", email="teste@test")
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == "donati"))

    assert user.username == "donati"
