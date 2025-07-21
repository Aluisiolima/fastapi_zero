from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core import exceptions
from fastapi_zero.core.repository import Category


class CategoryService:
    @staticmethod
    @exceptions
    async def get_all_categories(
        *, limit: int, offset: int, db: AsyncSession
    ) -> list[Category]:
        stmt = select(Category).limit(limit=limit).offset(offset=offset)

        categories: list[Category] = await db.scalars(stmt)

        return categories
