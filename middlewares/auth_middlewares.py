from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException
from core.security import decode_access_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        open_routes = ["/docs", "/","/redoc", "/openapi.json", "/auth/login", "/auth/register"]

        if request.url.path in open_routes:
            return await call_next(request)
        
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer"):
            raise HTTPException(status_code=401, detail="missing or invalid token")

        token = auth_header.split(" ")[1]

        payload = decode_access_token(token)

        if not payload:
            raise HTTPException(status_code=401, detail="Invalid or expired token")
        
        request.state.user = {"username": payload.get("sub"), "role": payload.get("role")}
        return await call_next(request)



# -------- BECAUSE SECRET KEY IS NOT WORKING OTHERSIE ABOVE CODE IS CORRECT

# from starlette.middleware.base import BaseHTTPMiddleware
# from fastapi import Request, HTTPException

# PUBLIC_PATHS = ["/docs", "/openapi.json", "/login", "/register"]

# class AuthMiddleware(BaseHTTPMiddleware):
#     async def dispatch(self, request: Request, call_next):
#         if request.url.path in PUBLIC_PATHS:
#             return await call_next(request)

#         authorization: str = request.headers.get("Authorization")
#         if not authorization or not authorization.startswith("Bearer "):
#             raise HTTPException(status_code=401, detail="missing or invalid token")

#         return await call_next(request)


