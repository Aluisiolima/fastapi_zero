from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from fastapi_zero.core import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=True)
