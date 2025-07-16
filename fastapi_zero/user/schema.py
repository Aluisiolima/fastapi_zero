from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="User's email address")
    name: str = Field(..., description="User's name", max_length=50)
    password: str = Field(
        ..., description="User's password", min_length=8, max_length=50
    )
    contact: Optional[str] = Field(
        default=None, description="User's contact number", max_length=14
    )

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'email': 'emailexemplas@gmail.com',
                'name': 'John Doe',
                'password': 'password123',
                'contact': '12345678901',
            }
        }


class UserUpdate(BaseModel):
    id: int  # solucao ate o JWT
    email: Optional[EmailStr] = Field(None, description="User's email address")
    name: Optional[str] = Field(None, description="User's name", max_length=50)
    password: Optional[str] = Field(
        None, description="User's password", min_length=8, max_length=50
    )
    contact: Optional[str] = Field(
        None, description="User's contact number", max_length=14
    )

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'email': 'emailexemplas@gmail.com',
                'name': 'John Doe',
                'password': 'password123',
                'contact': '12345678901',
            }
        }


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    contact: Optional[str]

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'id': 1,
                'email': 'emailexemplas@gmail.com',
                'name': 'John Doe',
                'contact': '12345678901',
            }
        }


class UserAddress(BaseModel):
    id: int
    user_id: int
    street: str
    city: str
    state: str
    zip_code: str

    class Config:
        from_attributes = True
        json_schema_extra = {
            'example': {
                'id': 1,
                'user_id': 1,
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA',
                'zip': '12345',
            }
        }


class UserAddressCreate(BaseModel):
    user_id: int = Field(..., description='Id user')
    street: str = Field(..., description='Street address', max_length=100)
    city: str = Field(..., description='City', max_length=50)
    state: str = Field(..., description='State', max_length=50)
    zip_code: str = Field(..., description='ZIP code', max_length=10)


class UserAddressUpdate(BaseModel):
    street: Optional[str] = Field(
        None, description='Street address', max_length=100
    )
    city: Optional[str] = Field(None, description='City', max_length=50)
    state: Optional[str] = Field(None, description='State', max_length=50)
    zip_code: Optional[str] = Field(
        None, description='ZIP code', max_length=10
    )
