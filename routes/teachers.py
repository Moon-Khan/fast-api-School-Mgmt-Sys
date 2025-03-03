from schemas import TeacherCreate, TeacherResponse
from fastapi import APIRouter, Depends
from typing import List
from services.teacher import create_teacher, get_all_teacher, get_teacher, update_teacher, delete_teacher
from dependencies.auth import check_teacher, check_admin

router = APIRouter()

@router.post("/add-teacher", response_model=TeacherResponse)
async def add_teacher(teacher_data:TeacherCreate, teach:dict = Depends(check_admin)):
    return await create_teacher(teacher_data)

@router.get("/fetch-all-teachers", response_model=List[TeacherResponse])
async def fetch_all_teacher(teach:dict = Depends(check_teacher)):
    return await get_all_teacher()

@router.get("/fetch-teacher/{teacher_id}", response_model=TeacherResponse)
async def fetch_teacher(teacher_id: str, teach:dict = Depends(check_teacher)):
    return await get_teacher(teacher_id)

@router.put("/update-teacher/{teacher_id}", response_model=TeacherResponse)
async def teacher_update(teacher_id: str, teacher:TeacherCreate, teach:dict = Depends(check_admin)):
    return await update_teacher(teacher_id, teacher)

@router.delete("/delete-teacher/{teacher_id}")
async def teacher_delete(teacher_id: str, teach:dict = Depends(check_admin)):
    return await delete_teacher(teacher_id)