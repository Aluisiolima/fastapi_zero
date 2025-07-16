from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from fastapi_zero.core.repository import Product, User

from fastapi_zero.core import BaseModel


class Order(BaseModel):
    __tablename__ = 'orders'

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('users.id'), nullable=False
    )
    status: Mapped[str] = mapped_column(
        String, nullable=False, default='Pendente'
    )

    user: Mapped['User'] = relationship('User', back_populates='orders')
    order_items: Mapped[list['OrdersItem']] = relationship(
        'OrdersItem', back_populates='order', cascade='all, delete-orphan'
    )


class OrdersItem(BaseModel):
    __tablename__ = 'orders_items'

    order_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('orders.id'), nullable=False
    )
    product_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('products.id'), nullable=False
    )
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    discount: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)

    order: Mapped['Order'] = relationship(
        'Order', back_populates='order_items'
    )
    product: Mapped['Product'] = relationship(
        'Product', back_populates='order_items'
    )
