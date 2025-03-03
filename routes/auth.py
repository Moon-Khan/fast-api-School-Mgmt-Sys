from services.auth import register_user, login_user
from schemas import CreateUser, UserResponse
from fastapi import FastAPI

router = FastAPI()

@router.post("/register", response_model=UserResponse)
async def register(user:CreateUser):
    return await register_user(user)

@router.post("/login")
async def login(email: str, pswrd: str):
    return await login_user(email, pswrd)

