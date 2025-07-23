from pydantic import Field

from fastapi_zero.core import SchemaBase


class LoginSchema(SchemaBase):
    email: str = Field(..., description='email from user')
    name: str = Field(..., description='name from user')
    password: str = Field(..., description='password from user')


class LoginResponse(SchemaBase):
    access_token: str
    token_type: str
