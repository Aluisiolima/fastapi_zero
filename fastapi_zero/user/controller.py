from fastapi import APIRouter,  HTTPException

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "name": "John Doe"}