from fastapi import FastAPI
from routes import students, teachers, courses, auth
from middlewares.auth_middlewares import AuthMiddleware

app = FastAPI(title="School Management System", version="1.0")

app.add_middleware(AuthMiddleware)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(teachers.router, prefix="/teachers", tags=["Teachers"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])


@app.get("/")
async def home():
    return {"message": "Welcome to the School Management System!"}

