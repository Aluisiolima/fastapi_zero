from decimal import Decimal
from typing import Optional

from pydantic import Field, field_validator

from fastapi_zero.core import SchemaBase


class ProductCreated(SchemaBase):
    name: str = Field(..., description='name product')
    price: Decimal = Field(..., description='price actual product')
    description: str = Field(..., description='description of product')
    discount: int = Field(0, description='discount applied in product')
    stock: int = Field(0, description='stock of product')

    @field_validator('name')
    @classmethod
    def to_lowercase(cls, v: str) -> str:
        return v.lower()


class ProductUpdate(SchemaBase):
    name: Optional[str] = Field(None, description='name product')
    price: Optional[Decimal] = Field(None, description='price actual product')
    description: Optional[str] = Field(
        None, description='description of product'
    )
    discount: Optional[int] = Field(
        None, description='discount applied in product'
    )
    stock: Optional[int] = Field(None, description='stock of product')

    @field_validator('name')
    @classmethod
    def to_lowercase(cls, v: str) -> str:
        return v.lower()


class ProductResponse(SchemaBase):
    id: int = Field(..., description='id product')
    name: str = Field(..., description='name product')
    price: Decimal = Field(..., description='price actual product')
    description: str = Field(..., description='description of product')
    discount: int = Field(..., description='discount applied in product')
    stock: int = Field(..., description='stock of product')
