from decimal import Decimal
from typing import Optional

from pydantic import Field

from fastapi_zero.core import SchemaBase


class ProductCreated(SchemaBase):
    name: str = Field(..., description='name product')
    price: Decimal = Field(..., description='price actual product')
    description: str = Field(..., description='description of product')
    discount: int = Field(
        ..., description='discount applied in product', default=0
    )
    stock: int = Field(..., description='stock of product', default=0)


class ProductUpdate(SchemaBase):
    name: Optional[str] = Field(..., description='name product')
    price: Optional[Decimal] = Field(..., description='price actual product')
    description: Optional[str] = Field(
        ..., description='description of product'
    )
    discount: Optional[int] = Field(
        ..., description='discount applied in product', default=None
    )
    stock: Optional[int] = Field(
        ..., description='stock of product', default=None
    )


class ProductResponse(SchemaBase):
    id: int = Field(..., description='id product')
    name: str = Field(..., description='name product')
    price: Decimal = Field(..., description='price actual product')
    description: str = Field(..., description='description of product')
    discount: int = Field(..., description='discount applied in product')
    stock: int = Field(..., description='stock of product')
