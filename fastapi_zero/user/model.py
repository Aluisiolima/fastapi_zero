from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped

from fastapi_zero.core import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = Column(String, unique=True, index=True)
    name: Mapped[str] = Column(String)
