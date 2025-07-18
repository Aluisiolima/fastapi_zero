from pydantic import Field

from fastapi_zero.core import SchemaBase


class CartCreatedItem(SchemaBase):
    user_id: int = Field(..., description='Id of user')
    product_id: int = Field(..., description='Id of product')
    quantity: int = Field(..., description='quantity of product')


class CartUpdateItem(SchemaBase):
    quantity: int = Field(..., description='quantity of product')


class CartResponse(SchemaBase):
    id: int
    user_id: int
    product_id: int
    quantity: int
