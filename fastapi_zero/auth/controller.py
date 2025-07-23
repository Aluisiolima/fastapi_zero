from http import HTTPStatus

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.auth.schema import LoginResponse
from fastapi_zero.auth.service import LoginService
from fastapi_zero.core.db import db

router = APIRouter()


@router.post('/login', status_code=HTTPStatus.OK, response_model=LoginResponse)
async def login(
    login: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(db.get_session),
):
    return await LoginService.login(login=login, db=db)
