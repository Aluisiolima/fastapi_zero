from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get('/me', status_code=HTTPStatus.OK)
async def get_user(): ...


@router.put('/me', status_code=HTTPStatus.NO_CONTENT)
async def update_user(user: dict): ...


@router.get('/me/addresses', status_code=HTTPStatus.OK)
async def get_user_addresses(): ...


@router.post('/me/addresses', status_code=HTTPStatus.CREATED)
async def create_user_address(address: dict): ...
