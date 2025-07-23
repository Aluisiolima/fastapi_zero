from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import Address, User
from fastapi_zero.core.security import JWT
from fastapi_zero.user.schema import (
    UserAddressCreate,
    UserAddressUpdate,
    UserCreate,
    UserUpdate,
)


class UserService:
    @staticmethod
    @exceptions
    async def create_user(
        *, user_create: UserCreate, db: AsyncSession
    ) -> User:
        user = User(**user_create.model_dump())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    @exceptions
    async def list_user(
        *, limit: int, offset: int, db: AsyncSession
    ) -> list[User]:
        stmt = select(User).offset(offset=offset).limit(limit=limit)
        users: list[User] = await db.scalars(stmt)

        return users

    @staticmethod
    @exceptions
    async def get_user_by_id(*, id: int, db: AsyncSession, token: JWT) -> User:
        if token.id != id and not token.is_adm:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )

        user: User = await db.get(User, id)

        return user

    @staticmethod
    @exceptions
    async def update_user(
        *, user_update: UserUpdate, db: AsyncSession, token: JWT
    ) -> None:
        if token.id != user_update.id and not token.is_adm:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )

        user_exist: User = await db.get(User, user_update.id)
        if not user_exist:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='User not found'
            )

        update_data = user_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user_exist, key, value)

        await db.commit()

    @staticmethod
    @exceptions
    async def get_user_address(
        *, id: int, db: AsyncSession, token: JWT
    ) -> list[Address]:
        if token.id != id and not token.is_adm:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )

        stmt = select(Address).where(Address.user_id == id)
        addresses: list[Address] = await db.scalars(stmt)

        return addresses

    @staticmethod
    @exceptions
    async def create_address_user(
        *, address_create: UserAddressCreate, db: AsyncSession, token: JWT
    ) -> Address:
        if token.id != address_create.user_id and not token.is_adm:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )

        stmt = select(Address).where(
            and_(
                Address.user_id == address_create.user_id,
                Address.state == address_create.state,
                Address.city == address_create.city,
                Address.street == address_create.street,
            )
        )

        address_exist: Address = await db.scalar(stmt)

        if address_exist:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail='The address already exist',
            )

        address = Address(**address_create.model_dump())

        db.add(address)
        await db.commit()
        await db.refresh(address)

        return address

    @staticmethod
    @exceptions
    async def update_address(
        *,
        id: int,
        address_update: UserAddressUpdate,
        db: AsyncSession,
        token: JWT,
    ) -> None:
        if token.id != id and not token.is_adm:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )
        address_exist: Address = await db.get(Address, id)
        if not address_exist:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='User not found'
            )

        update_data = address_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(address_exist, key, value)

        await db.commit()
        await db.refresh(address_exist)

    @staticmethod
    @exceptions
    async def delete_address(*, id: int, db: AsyncSession, token: JWT) -> None:
        if token.id != id and not token.is_adm:
            raise HTTPException(
                status_code=HTTPStatus.FORBIDDEN,
                detail='Not enough permissions',
            )
        address = await db.get(Address, id)

        if not address:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='Address not found'
            )

        await db.delete(address)
        await db.commit()
