from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core.db import PostgresDB
from fastapi_zero.user.schema import (
    UserAddress,
    UserAddressCreate,
    UserAddressUpdate,
    UserCreate,
    UserResponse,
    UserUpdate,
)
from fastapi_zero.user.service import UserService

router = APIRouter()
db = PostgresDB()


@router.post('/', status_code=HTTPStatus.CREATED, response_model=UserResponse)
async def create_user(
    user: UserCreate, db: AsyncSession = Depends(db.get_session)
):
    user = await UserService.create_user(user_create=user, db=db)
    return user


@router.get('/me', status_code=HTTPStatus.OK, response_model=UserResponse)
async def get_user(db: AsyncSession = Depends(db.get_session)): ...


@router.put('/me', status_code=HTTPStatus.NO_CONTENT)
async def update_user(
    user: UserUpdate, db: AsyncSession = Depends(db.get_session)
): ...


@router.get(
    '/me/addresses',
    status_code=HTTPStatus.OK,
    response_model=list[UserAddress],
)
async def get_user_addresses(db: AsyncSession = Depends(db.get_session)): ...


@router.post(
    '/me/addresses', status_code=HTTPStatus.CREATED, response_model=UserAddress
)
async def create_user_address(
    address: UserAddressCreate, db: AsyncSession = Depends(db.get_session)
): ...


@router.put('/me/addresses/{id_address}', status_code=HTTPStatus.NO_CONTENT)
async def update_user_address(
    id_address: int,
    address: UserAddressUpdate,
    db: AsyncSession = Depends(db.get_session),
): ...
