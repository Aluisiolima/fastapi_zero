from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.auth.schema import LoginSchema
from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import User
from fastapi_zero.core.security import encode_to, verify_password


class LoginService:
    @staticmethod
    @exceptions
    async def login(*, login: LoginSchema, db: AsyncSession):
        stmt = select(User).where(
            and_(User.email == login.email, User.name == login.name)
        )

        user: User = await db.scalar(stmt)

        if not user:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='User not found'
            )

        if not user.is_active:
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='User not active'
            )

        if not verify_password(login.password, user.password):
            raise HTTPException(
                status_code=HTTPStatus.UNAUTHORIZED, detail='User data invalid'
            )

        return {
            'token': encode_to({
                'id': user.id,
                'name': user.name,
                'is_adm': user.is_adm,
            })
        }
