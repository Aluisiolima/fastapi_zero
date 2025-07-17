from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import Product
from fastapi_zero.produto.schema import ProductCreated, ProductUpdate


class ProductServices:
    @staticmethod
    @exceptions
    async def list_product(
        *, offset: int, limit: int, db: AsyncSession
    ) -> list[Product]:
        stmt = select(Product).offset(offset=offset).limit(limit=limit)
        products: list[Product] = await db.scalars(stmt)

        return products

    @staticmethod
    @exceptions
    async def get_product_by_id(*, id: int, db: AsyncSession) -> Product:
        product: Product = await db.get(Product, id)

        if not product:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='NotFound Product'
            )

        return product

    @staticmethod
    @exceptions
    async def created_product(
        *, product: ProductCreated, db: AsyncSession
    ) -> Product:
        product = Product(**product.model_dump())
        db.add(product)
        await db.commit()
        await db.refresh(product)

        return product

    @staticmethod
    @exceptions
    async def updated_product(
        *, id: int, product: ProductUpdate, db: AsyncSession
    ) -> None:
        product_exist: Product = await db.get(Product, id)
        if not product_exist:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='NotFound Product'
            )

        update_data = product.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(product_exist, key, value)

        await db.commit()

    @staticmethod
    @exceptions
    async def deleted_product(*, id: int, db: AsyncSession) -> None:
        product_exist = await db.get(Product, id)

        if not product_exist:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND, detail='NotFound Product'
            )

        await db.delete(product_exist)
        await db.commit()

    @staticmethod
    @exceptions
    async def search_product(*, name: str, db: AsyncSession) -> list[Product]:
        stmt = select(Product).where(Product.name.like(f'%{name}%'))
        products: list[Product] = await db.scalars(stmt)

        return products
