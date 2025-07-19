from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import Order, OrdersItem, Product
from fastapi_zero.pedido.schema import OrderCreate, Status


class OrderService:
    @staticmethod
    @exceptions
    async def created_order(*, order: OrderCreate, db: AsyncSession) -> Order:
        new_order = Order(user_id=order.user_id, status=order.status)
        db.add(new_order)
        await db.flush()

        for item in order.itens:
            product = await db.get(Product, item.product_id)

            if not product:
                raise HTTPException(
                    status_code=HTTPStatus.NOT_FOUND, detail='NotFound Product'
                )

            order_item = OrdersItem(
                order_id=new_order.id,
                product_id=product.id,
                price=product.price,
                discount=product.discount,
                quantity=item.quantity,
            )
            db.add(order_item)
            product.stock -= item.quantity

        await db.commit()
        await db.refresh(new_order)

        return new_order

    @staticmethod
    @exceptions
    async def get_order(*, id: int, db: AsyncSession) -> Order:
        stmt = (
            select(Order)
            .options(selectinload(Order.order_items))
            .where(Order.id == id)
        )

        order: Order = await db.scalar(stmt)

        if not order:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='Not Found Order'
            )

        return order

    @staticmethod
    @exceptions
    async def get_all_order(*, user_id: int, db: AsyncSession) -> list[Order]:
        stmt = (
            select(Order)
            .options(selectinload(Order.order_items))
            .where(Order.user_id == user_id)
        )

        result = await db.scalars(stmt)
        orders: Order = result.all()

        return orders

    @staticmethod
    @exceptions
    async def cancel_order(*, id: int, db: AsyncSession) -> None:
        stmt = (
            select(Order)
            .options(selectinload(Order.order_items))
            .where(Order.id == id)
        )

        order: Order = await db.scalar(stmt)

        if not order:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='Not Found Order'
            )

        if order.status != Status.PENDENTE:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail='Not possible cancel order',
            )

        order.status = Status.CANCELADO

        for item in order.order_items:
            product = await db.get(Product, item.product_id)

            product.stock += item.quantity

        await db.commit()
