from typing import Optional

from pydantic import EmailStr, Field, field_validator

from fastapi_zero.core import SchemaBase
from fastapi_zero.core.security import hash_password


class UserCreate(SchemaBase):
    email: EmailStr = Field(..., description="User's email address")
    name: str = Field(..., description="User's name", max_length=50)
    password: str = Field(
        ..., description="User's password", min_length=8, max_length=255
    )
    contact: Optional[str] = Field(
        default=None, description="User's contact number", max_length=14
    )

    @field_validator('password', mode='before')
    @classmethod
    def hash(cls, v: str) -> str:
        try:
            return hash_password(password=v)
        except Exception as e:
            print(e)


class UserUpdate(SchemaBase):
    id: int  # solucao ate o JWT
    email: Optional[EmailStr] = Field(None, description="User's email address")
    name: Optional[str] = Field(None, description="User's name", max_length=50)
    password: Optional[str] = Field(
        None, description="User's password", min_length=8, max_length=255
    )
    contact: Optional[str] = Field(
        None, description="User's contact number", max_length=14
    )

    @field_validator('password', mode='before')
    @classmethod
    def hash(cls, v: str | None) -> str | None:
        if v:
            return hash_password(password=v)

        return None


class UserResponse(SchemaBase):
    id: int
    email: EmailStr
    name: str
    contact: Optional[str]


class UserAddress(SchemaBase):
    id: int
    user_id: int
    street: str
    city: str
    state: str
    zip_code: str


class UserAddressCreate(SchemaBase):
    user_id: int = Field(..., description='Id user')
    street: str = Field(..., description='Street address', max_length=100)
    city: str = Field(..., description='City', max_length=50)
    state: str = Field(..., description='State', max_length=50)
    zip_code: str = Field(..., description='ZIP code', max_length=10)


class UserAddressUpdate(SchemaBase):
    street: Optional[str] = Field(
        None, description='Street address', max_length=100
    )
    city: Optional[str] = Field(None, description='City', max_length=50)
    state: Optional[str] = Field(None, description='State', max_length=50)
    zip_code: Optional[str] = Field(
        None, description='ZIP code', max_length=10
    )
