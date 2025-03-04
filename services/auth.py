from core.security import hash_pswrd,verify_pswrd, create_access_token
from models import users
from schemas import CreateUser, UserResponse
from fastapi import HTTPException



async def register_user(user:CreateUser):
    user_find = await users.find_one({"username":user.username})
    if user_find:
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_data = user.dict()
    user_data["password"]=hash_pswrd(user.password)
    result = await users.insert_one(user_data)

    return UserResponse(**user_data,id= str(result.inserted_id) )

async def login_user(username:str, pswrd: str):
    user_find = await users.find_one({"username": username})

    if not user_find:
        raise HTTPException(status_code=404, detail="User not found")

    pswrd_check = verify_pswrd(pswrd, user_find["password"] )

    if not pswrd_check:
        raise HTTPException(status_code=481, detail="password not correct")
    
    token_create = create_access_token({"sub": user_find["username"], "role": user_find["role"]})

    return {"access_token": token_create, "token_type": "bearer"}
