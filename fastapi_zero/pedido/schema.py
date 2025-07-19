from enum import Enum

from pydantic import Field, field_validator

from fastapi_zero.core import SchemaBase


class OrderItem(SchemaBase):
    product_id: int
    quantity: int


class Status(str, Enum):
    PENDENTE = 'pendente'
    ENTREGUE = 'entregue'
    SAIU_PARA_ENTREGUE = 'saiu para entregue'
    CANCELADO = 'cancelado'


class OrderCreate(SchemaBase):
    user_id: int = Field(..., description='Id user')
    status: Status = Field(..., description='Order status')
    itens: list[OrderItem]

    @field_validator('status')
    @classmethod
    def to_lowercase(cls, v: str) -> str:
        return v.lower()


class OrderResponse(SchemaBase):
    id: int
    user_id: int
    status: Status
    order_items: list[OrderItem]
