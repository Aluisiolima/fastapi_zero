from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.cart.schema import (
    CartCreatedItem,
    CartResponse,
    CartUpdateItem,
)
from fastapi_zero.cart.service import CartService
from fastapi_zero.core.db import db

router = APIRouter()


# TODO: id passado pela url ate o token JWT
@router.get(
    '/{cart_id}', status_code=HTTPStatus.OK, response_model=list[CartResponse]
)
async def get_cart(cart_id: int, db: AsyncSession = Depends(db.get_session)):
    return await CartService.get_cart(user_id=cart_id, db=db)


@router.post(
    '/items', status_code=HTTPStatus.CREATED, response_model=CartResponse
)
async def create_cart(
    cart: CartCreatedItem, db: AsyncSession = Depends(db.get_session)
):
    return await CartService.created_cart_item(created_item=cart, db=db)


@router.put('/items/{cart_id}', status_code=HTTPStatus.NO_CONTENT)
async def update_cart(
    cart_id: int,
    cart: CartUpdateItem,
    db: AsyncSession = Depends(db.get_session),
):
    await CartService.update_cart(cart_id=cart_id, cart_update=cart, db=db)


@router.delete('/items/{cart_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_cart(
    cart_id: int, db: AsyncSession = Depends(db.get_session)
):
    await CartService.deleted_cart(id=cart_id, db=db)
