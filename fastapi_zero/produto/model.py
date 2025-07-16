from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, Numeric, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_zero.core import BaseModel

if TYPE_CHECKING:
    from fastapi_zero.core.repository import (
        Cart,
        Category,
        OrdersItem,
        ProductCategory,
    )


class Product(BaseModel):
    __tablename__ = 'products'

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    discount: Mapped[int] = mapped_column(SmallInteger, default=0)
    stock: Mapped[int] = mapped_column(Integer, default=0)

    categories: Mapped[list['ProductCategory']] = relationship(
        back_populates='product', cascade='all, delete-orphan'
    )
    carts: Mapped[list['Cart']] = relationship(back_populates='product')
    order_items: Mapped[list['OrdersItem']] = relationship(
        back_populates='product', cascade='all, delete-orphan'
    )


class ProductCategory(BaseModel):
    __tablename__ = 'products_categories'

    product_id: Mapped[int] = mapped_column(
        ForeignKey('products.id'), primary_key=True
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey('categories.id'), primary_key=True
    )

    category: Mapped['Category'] = relationship(back_populates='products')
    product: Mapped['Product'] = relationship(back_populates='categories')
