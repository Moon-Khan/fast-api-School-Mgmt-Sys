from schemas import CourseCreate, CourseResponse
from fastapi import HTTPException
from models import courses
from typing import List
from bson import ObjectId



async def create_course(course_data:CourseCreate) ->CourseResponse:
    coursedata=course_data.dict()
    result = await courses.insert_one(coursedata)

    if not result.inserted_id:
        raise HTTPException (status_code=500, detail= "course not created")
    
    return CourseResponse(**coursedata, id=str(result.inserted_id))


async def get_all_courses() ->List[CourseResponse]:
    courses_list=[]

    async for course in courses.find():
        course["id"]=str(course["_id"])
        courses_list.append(CourseResponse(**course))

    return courses_list


async def get_course(course_id: str) -> CourseResponse:
    course = await courses.find_one({"_id":ObjectId(course_id)})        

    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    course["id"] = str(course.pop("_id")) 
    return CourseResponse(**course)



async def update_course(course_id:str, course:CourseCreate)->CourseResponse:
    courseid=ObjectId(course_id)
    updated_data = await courses.update_one({"_id":courseid}, {"$set":course.dict()})   

    if updated_data.modified_count == 0:
        raise HTTPException(status_code=404, detail="course not found")
    
    course_updated = await courses.find_one({"_id": courseid})
    course_updated["id"]=str(course_updated["_id"])
    return CourseResponse(**course_updated)



async def delete_course(course_id:str):
    courseid=ObjectId(course_id)
    delete_result = await courses.delete_one({"_id":courseid})
    
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="course not found")
    
    return ("course deleted")