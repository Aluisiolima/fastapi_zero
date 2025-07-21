from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core.db import db
from fastapi_zero.pedido.schema import OrderCreate, OrderResponse
from fastapi_zero.pedido.service import OrderService

router = APIRouter()


@router.post('/', status_code=HTTPStatus.CREATED, response_model=OrderResponse)
async def create_pedido(
    order: OrderCreate, db: AsyncSession = Depends(db.get_session)
):
    return await OrderService.created_order(order=order, db=db)


@router.get(
    '/{pedido_id}', status_code=HTTPStatus.OK, response_model=OrderResponse
)
async def get_pedido_by_id(
    pedido_id: int, db: AsyncSession = Depends(db.get_session)
):
    return await OrderService.get_order(id=pedido_id, db=db)


@router.get(
    '/user/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=list[OrderResponse],
)
async def get_pedidos(
    user_id: int,
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(db.get_session),
):
    return await OrderService.get_all_order(
        user_id=user_id, limit=limit, offset=offset, db=db
    )


@router.delete('/{pedido_id}/cancel', status_code=HTTPStatus.NO_CONTENT)
async def cancel_pedido(
    pedido_id: int, db: AsyncSession = Depends(db.get_session)
):
    await OrderService.cancel_order(id=pedido_id, db=db)
