from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_zero.core import BaseModel

if TYPE_CHECKING:
    from fastapi_zero.core.repository import ProductCategory


class Category(BaseModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    products: Mapped[list['ProductCategory']] = relationship(
        back_populates='category', cascade='all, delete-orphan'
    )
