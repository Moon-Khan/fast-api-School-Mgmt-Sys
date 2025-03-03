from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import secrets


SECRET_KEY= secrets.token_hex(32)
ACCESS_TOKEN_EXPIRE_MINUTES=30
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pswrd(pswrd: str) ->str:
    return pwd_context.hash(pswrd)

def verify_pswrd(plain_pswrd: str, hash_pswrd: str) ->bool:
    return pwd_context.verify(plain_pswrd, hash_pswrd)

def create_access_token(data: dict):
    to_encode = data.copy   ()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        return payload
    
    except JWTError:
        return None
