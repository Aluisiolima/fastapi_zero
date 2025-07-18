from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.cart.schema import CartCreatedItem, CartUpdateItem
from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import Cart, Product


class CartService:
    @staticmethod
    @exceptions
    async def get_cart(*, user_id: int, db: AsyncSession) -> list[Cart]:
        stmt = select(Cart).where(Cart.user_id == user_id)
        cart: list[Cart] = await db.scalars(stmt)

        return cart

    @staticmethod
    @exceptions
    async def created_cart_item(
        *, created_item: CartCreatedItem, db: AsyncSession
    ) -> Cart:
        product: Product = await db.get(Product, created_item.product_id)

        if product.stock < created_item.quantity:
            raise HTTPException(
                status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
                detail='Quantity order is more than quantity in stock',
            )

        cart = Cart(**created_item.model_dump())

        db.add(cart)
        await db.commit()
        await db.refresh(cart)

        return cart

    @staticmethod
    @exceptions
    async def update_cart(
        *, cart_id: int, cart_update: CartUpdateItem, db: AsyncSession
    ) -> None:
        cart_exist: Cart = await db.get(Cart, cart_id)

        if not cart_exist:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='NotFound cart'
            )

        update_data = cart_update.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(cart_exist, key, value)

        await db.commit()

    @staticmethod
    @exceptions
    async def deleted_cart(*, id: int, db: AsyncSession) -> None:
        cart_exist: Cart = await db.get(Cart, id)

        if not cart_exist:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='NotFound cart'
            )

        await db.delete(cart_exist)
        await db.commit()
