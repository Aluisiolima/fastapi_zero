from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.core.db import db
from fastapi_zero.produto.schema import (
    ProductCreated,
    ProductResponse,
    ProductUpdate,
)
from fastapi_zero.produto.service import ProductServices

router = APIRouter()


@router.get(
    '/search', status_code=HTTPStatus.OK, response_model=list[ProductResponse]
)
async def search_produto(
    name: str = Query(..., min_length=1),
    db: AsyncSession = Depends(db.get_session),
):
    return await ProductServices.search_product(name=name.lower(), db=db)


@router.get(
    '/', status_code=HTTPStatus.OK, response_model=list[ProductResponse]
)
async def get_produtos(
    offset: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    db: AsyncSession = Depends(db.get_session),
):
    return await ProductServices.list_product(
        offset=offset, limit=limit, db=db
    )


@router.get(
    '/{produto_id}', status_code=HTTPStatus.OK, response_model=ProductResponse
)
async def get_produto_by_id(
    produto_id: int, db: AsyncSession = Depends(db.get_session)
):
    return await ProductServices.get_product_by_id(id=produto_id, db=db)


@router.post(
    '/', status_code=HTTPStatus.CREATED, response_model=ProductResponse
)
async def create_produto(
    product: ProductCreated, db: AsyncSession = Depends(db.get_session)
):
    return await ProductServices.created_product(product=product, db=db)


@router.put('/{produto_id}', status_code=HTTPStatus.NO_CONTENT)
async def update_produto(
    produto_id: int,
    produto: ProductUpdate,
    db: AsyncSession = Depends(db.get_session),
):
    await ProductServices.updated_product(
        id=produto_id, product=produto, db=db
    )


@router.delete('/{produto_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_produto(
    produto_id: int, db: AsyncSession = Depends(db.get_session)
):
    await ProductServices.deleted_product(id=produto_id, db=db)
