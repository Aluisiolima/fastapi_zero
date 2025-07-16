from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_zero.core import BaseModel

if TYPE_CHECKING:
    from fastapi_zero.core.repository import Product, User


class Cart(BaseModel):
    __tablename__ = 'cart'

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('users.id'), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('products.id'), nullable=False
    )
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    user: Mapped['User'] = relationship(back_populates='carts')
    product: Mapped['Product'] = relationship(back_populates='carts')
