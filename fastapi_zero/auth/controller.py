from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/login")
async def login(username: str, password: str):
    ...

@router.post("/register")
async def register(user: dict):
    ... 