from jwt import decode

from config.security import create_access_token
from config.settings import Settings


def test_jwt():
    data = {"test": "test"}
    token = create_access_token(data)

    decoded = decode(token, Settings().SECRET_KEY, algorithms=["HS256"])

    assert decoded["test"] == data["test"]
    assert "exp" in decoded
