from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get('/', status_code=HTTPStatus.OK)
async def get_categoria(): ...
