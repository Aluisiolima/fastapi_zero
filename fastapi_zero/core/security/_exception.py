from http import HTTPStatus

from fastapi import HTTPException
from jwt.exceptions import (
    DecodeError,
    ExpiredSignatureError,
    InvalidSignatureError,
    InvalidTokenError,
    MissingRequiredClaimError,
)


class ExceptionsJwt:
    @staticmethod
    def handle_exception(exc):
        if isinstance(exc, DecodeError):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail=('Esse token ta igual tua cara'),
                headers={'WWW-Authenticate': 'Bearer'},
            )
        elif isinstance(exc, ExpiredSignatureError):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail=('Vixi o token da vencido já, vai dar não'),
                headers={'WWW-Authenticate': 'Bearer'},
            )
        elif isinstance(exc, MissingRequiredClaimError):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail=('Não ta faltando alguma coisa nesse Token não?'),
                headers={'WWW-Authenticate': 'Bearer'},
            )

        elif isinstance(exc, InvalidTokenError):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail=('Uhum não gostei de você não, autorização negada'),
                headers={'WWW-Authenticate': 'Bearer'},
            )

        elif isinstance(exc, InvalidSignatureError):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail=('Esse token não tem galantia'),
                headers={'WWW-Authenticate': 'Bearer'},
            )
        else:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED,
                detail=f'{exc}',
                headers={'WWW-Authenticate': 'Bearer'},
            )


def exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            ExceptionsJwt.handle_exception(e)

    return wrapper
