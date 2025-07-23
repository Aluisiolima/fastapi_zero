from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core.db import db
from fastapi_zero.core.security import extract_token_header
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


@router.post(
    '/register', status_code=HTTPStatus.CREATED, response_model=UserResponse
)
async def create_user(
    user: UserCreate, db: AsyncSession = Depends(db.get_session)
):
    return await UserService.create_user(user_create=user, db=db)


@router.post('/', status_code=HTTPStatus.OK, response_model=list[UserResponse])
async def get_user(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: AsyncSession = Depends(db.get_session),
    token: dict = Depends(extract_token_header),
):
    return await UserService.list_user(limit=limit, offset=offset, db=db)


@router.get('/me/{id}', status_code=HTTPStatus.OK, response_model=UserResponse)
async def get_user_by_id(id: int, db: AsyncSession = Depends(db.get_session)):
    return await UserService.get_user_by_id(id=id, db=db)


@router.put('/me', status_code=HTTPStatus.NO_CONTENT)
async def update_user(
    user: UserUpdate, db: AsyncSession = Depends(db.get_session)
):
    await UserService.update_user(user_update=user, db=db)


@router.get(
    '/me/addresses/{id}',
    status_code=HTTPStatus.OK,
    response_model=list[UserAddress],
)
async def get_user_addresses(
    id: int, db: AsyncSession = Depends(db.get_session)
):
    return await UserService.get_user_address(id=id, db=db)


@router.post(
    '/me/addresses', status_code=HTTPStatus.CREATED, response_model=UserAddress
)
async def create_user_address(
    address: UserAddressCreate, db: AsyncSession = Depends(db.get_session)
):
    return await UserService.create_address_user(address_create=address, db=db)


@router.put('/me/addresses/{id_address}', status_code=HTTPStatus.NO_CONTENT)
async def update_user_address(
    id_address: int,
    address: UserAddressUpdate,
    db: AsyncSession = Depends(db.get_session),
):
    await UserService.update_address(
        id=id_address, address_update=address, db=db
    )


@router.delete('/me/addresses/{id_address}', status_code=HTTPStatus.NO_CONTENT)
async def delete_user_address(
    id_address: int,
    db: AsyncSession = Depends(db.get_session),
):
    await UserService.delete_address(id=id_address, db=db)
