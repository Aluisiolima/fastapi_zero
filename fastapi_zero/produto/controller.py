from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/{produto_id}")
async def get_produto(produto_id: int):
    return {"produto_id": produto_id, "items": []}