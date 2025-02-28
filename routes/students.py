from schemas import StudentCreate, StudentResponse
from fastapi import APIRouter
from typing import List
from services.student import create_student, get_all_students, get_student, update_student,delete_student


router = APIRouter()

@router.post("/add-student", response_model=StudentResponse)
async def add_student(student:StudentCreate):
    return await create_student(student)

@router.get("/fetch-all-students", response_model=List[StudentResponse])
async def fetch_all_students():
    return await get_all_students()

@router.get("/fetch-student/{student_id}", response_model=StudentResponse)
async def fetch_student(student_id: str):
    return await get_student(student_id)

@router.put("/update-student/{student_id}", response_model=StudentResponse)
async def student_update(student_id: str, student:StudentResponse):
    return await update_student(student_id, student)

@router.delete("/delete-student/{student_id}")
async def student_delete(student_id: str):
    return await delete_student(student_id)

