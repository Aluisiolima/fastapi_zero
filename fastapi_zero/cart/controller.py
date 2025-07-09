from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/{cart_id}")
async def get_cart(cart_id: int):
    return {"cart_id": cart_id, "items": []}