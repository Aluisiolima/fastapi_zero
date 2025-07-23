from http import HTTPStatus

from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import User
from fastapi_zero.core.security import encode_to, verify_password


class LoginService:
    @staticmethod
    @exceptions
    async def login(*, login: OAuth2PasswordRequestForm, db: AsyncSession):
        stmt = select(User).where(User.email == login.username)

        user: User = await db.scalar(stmt)

        if not user.is_active:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='User not active'
            )

        if not user or not verify_password(login.password, user.password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='User data invalid'
            )

        access_token = encode_to({
            'id': user.id,
            'name': user.name,
            'is_adm': user.is_adm,
        })

        return {'access_token': access_token, 'token_type': 'Bearer'}
