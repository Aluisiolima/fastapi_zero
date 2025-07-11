from datetime import UTC, datetime

from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core import exceptions
from fastapi_zero.user.model import User
from fastapi_zero.user.schema import UserCreate


class UserService:
    @staticmethod
    @exceptions
    async def create_user(*, user_create: UserCreate, db: AsyncSession):
        user = User(
            **user_create.model_dump(),
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
