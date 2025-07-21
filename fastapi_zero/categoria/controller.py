from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.categoria.schema import CategoryResponse
from fastapi_zero.categoria.service import CategoryService
from fastapi_zero.core.db import db

router = APIRouter()


@router.get(
    '/', status_code=HTTPStatus.OK, response_model=list[CategoryResponse]
)
async def get_categoria(
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db: AsyncSession = Depends(db.get_session),
):
    return await CategoryService.get_all_categories(
        limit=limit, offset=offset, db=db
    )
