from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from core.security import decode_access_token

auth_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Security(auth_scheme)):
    token_decode = decode_access_token(token)

    if not token_decode:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return token_decode

async def check_teacher(user:dict = Depends(get_current_user)):
    if user["role"]!="teacher":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user
    
async def check_student(user:dict = Depends(get_current_user)):
    if user["role"]!="student":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user

async def check_admin(user:dict = Depends(get_current_user)):
    if user["role"]!="admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return user
