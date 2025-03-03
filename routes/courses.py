from schemas import CourseCreate, CourseResponse
from fastapi import APIRouter, Depends
from typing import List
from services.course import create_course, get_all_courses, get_course, update_course, delete_course
from dependencies.auth import check_admin

router = APIRouter()

@router.post("/add-course", response_model=CourseResponse)
async def add_course(course_data:CourseCreate, admin: dict = Depends(check_admin)):
    return await create_course(course_data)

@router.get("/fetch-all-courses", response_model=List[CourseResponse])
async def fetch_all_courses():
    return await get_all_courses()

@router.get("/fetch-course/{course_id}", response_model=CourseResponse)
async def fetch_course(course_id: str):
    return await get_course(course_id)

@router.put("/update-course/{course_id}", response_model=CourseResponse)
async def course_udpate(course_id: str, course_data:CourseCreate, admin: dict = Depends(check_admin)):
    return await update_course(course_id, course_data)

@router.delete("/delete-course/{course_id}")
async def course_delete(course_id: str, admin: dict = Depends(check_admin)):
    return await delete_course(course_id)

    