from datetime import UTC, datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import decode, encode

from fastapi_zero.core import SchemaBase, Settings

from ._exception import exceptions

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')


class JWT(SchemaBase):
    id: int
    name: str
    is_adm: bool


@exceptions
def encode_to(date: dict) -> str:
    expire = datetime.now(UTC) + timedelta(days=Settings().EXPIRE)

    date.update({'exp': expire, 'iat': datetime.now(UTC)})
    return encode(date, Settings().SECRET_KEY, Settings().ALGORITHM)


@exceptions
def decode_to(token: str) -> JWT:
    return decode(
        token,
        Settings().SECRET_KEY,
        algorithms=[Settings().ALGORITHM],
        options={'require': ['exp', 'iat']},
    )


def extract_token_header(token: str = Depends(oauth2_scheme)) -> JWT:
    payload: JWT = decode_to(token)

    return JWT(**payload)
