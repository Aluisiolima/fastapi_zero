from fastapi import APIRouter, HTTPException
from http import HTTPStatus

router = APIRouter()

@router.get("/", status_code=HTTPStatus.OK)
async def get_produto():
    ...

@router.get("/{produto_id}", status_code=HTTPStatus.OK)
async def get_produto_by_id(produto_id: int):
    ...

@router.post("/", status_code=HTTPStatus.CREATED)
async def create_produto(produto: dict):
    ...

@router.put("/{produto_id}", status_code=HTTPStatus.NO_CONTENT)
async def update_produto(produto_id: int, produto: dict):
    ...

@router.delete("/{produto_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_produto(produto_id: int):
    ...

@router.get("/search", status_code=HTTPStatus.OK)
async def search_produto(query: str):
    ...