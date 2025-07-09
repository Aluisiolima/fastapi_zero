from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.post('/', status_code=HTTPStatus.CREATED)
async def create_pedido(pedido: dict): ...


@router.get('/{pedido_id}', status_code=HTTPStatus.OK)
async def get_pedido_by_id(pedido_id: int): ...


@router.get('/', status_code=HTTPStatus.OK)
async def get_pedidos(): ...


@router.delete('/{pedido_id}/cancel', status_code=HTTPStatus.NO_CONTENT)
async def cancel_pedido(pedido_id: int): ...
