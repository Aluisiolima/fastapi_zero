from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/{pedido_id}")
async def get_pedido(pedido_id: int):
    return {"pedido_id": pedido_id, "items": []}