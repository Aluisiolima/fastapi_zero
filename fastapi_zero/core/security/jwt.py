from datetime import UTC, datetime, timedelta

from jwt import decode, encode

from fastapi_zero.core import Settings


def encode_to(date: dict) -> str:
    expire = datetime.now(UTC) + timedelta(days=Settings().EXPIRE)

    date.update({'exp': expire, 'iat': datetime.now(UTC)})
    return encode(date, Settings().SECRET_KEY, Settings().ALGORITHM)


def deconde_to(token: str):
    return decode(
        token,
        Settings().SECRET_KEY,
        algorithms=[Settings().ALGORITHM],
        options={'require': ['exp', 'iat']},
    )
