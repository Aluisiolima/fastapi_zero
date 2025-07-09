from fastapi import APIRouter, HTTPException
from http import HTTPStatus

router = APIRouter()

@router.get("/", status_code=HTTPStatus.OK)
async def get_categoria():
    ...