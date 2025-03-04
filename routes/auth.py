from services.auth import register_user, login_user
from schemas import CreateUser, UserResponse
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter() 

@router.post("/register", response_model=UserResponse)
async def register(user:CreateUser):
    return await register_user(user)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_user(form_data.username, form_data.password)

