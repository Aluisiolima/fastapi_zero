from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.get('/', status_code=HTTPStatus.OK)
async def get_cart(cart_id: int): ...


@router.post('/items', status_code=HTTPStatus.CREATED)
async def create_cart(cart: dict): ...


@router.put('/items/{cart_id}', status_code=HTTPStatus.NO_CONTENT)
async def update_cart(cart_id: int, cart: dict): ...


@router.delete('/items/{cart_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_cart(cart_id: int): ...
