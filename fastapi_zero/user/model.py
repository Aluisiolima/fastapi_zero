from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from fastapi_zero.core import BaseModel

if TYPE_CHECKING:
    from fastapi_zero.core.repository import Address, Cart, Order


class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    contact: Mapped[str] = mapped_column(String(14), nullable=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True
    )
    is_adm: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False
    )

    addresses: Mapped[list['Address']] = relationship(
        'Address', back_populates='user', cascade='all, delete-orphan'
    )
    carts: Mapped[list['Cart']] = relationship(
        'Cart', back_populates='user', cascade='all, delete-orphan'
    )
    orders: Mapped[list['Order']] = relationship(
        'Order', back_populates='user', cascade='all, delete-orphan'
    )


class Address(BaseModel):
    __tablename__ = 'addresses'

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('users.id'), nullable=False
    )
    street: Mapped[str] = mapped_column(String(100), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)
    state: Mapped[str] = mapped_column(String(50), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10), nullable=False)

    user: Mapped['User'] = relationship('User', back_populates='addresses')
