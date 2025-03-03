from pydantic import BaseModel, EmailStr, Field
from typing import List

class TeacherCreate(BaseModel):
    name:str = Field(..., min_length=2,max_length=15)
    email: EmailStr
    phone_number: str = Field(..., pattern="^\\d{10}$")
    course_id : str

class TeacherResponse(TeacherCreate):
    id:str

class StudentCreate(BaseModel):
    name:str
    email: EmailStr
    age:int =Field(..., gt=5, lt=18)
    courses : List[str]

class StudentResponse(StudentCreate):
    id:str

class CourseCreate(BaseModel):
    name: str=Field(..., min_length=2,max_length=15)
    teacher_id: str
    students_id: List[str]

class CourseResponse(CourseCreate):
    id:str

class CreateUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

class UserResponse(CreateUser):
    id: str
    