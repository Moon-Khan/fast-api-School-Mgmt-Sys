from schemas import TeacherCreate, TeacherResponse
from fastapi import HTTPException
from models import teachers
from bson import ObjectId
from typing import List



async def create_teacher(teacher_data:TeacherCreate)-> TeacherResponse:
    teacherdata=teacher_data.dict()
    result = await teachers.insert_one(teacherdata)
    
    if not result.inserted_id:
        raise HTTPException (status_code=500, detail="teacher not created")
    
    return TeacherResponse(**teacherdata, id=str(result.inserted_id))



async def get_all_teacher()->List[TeacherResponse]:
    teachers_list=[]

    async for teacher in teachers.find():
        teacher["id"]=str(teacher["_id"])
        teachers_list.append(TeacherResponse(**teacher))

    return teachers_list



async def get_teacher(teacher_id: str) ->TeacherResponse:
    teacher = await teachers.find_one({"_id":ObjectId(teacher_id)})

    if not teacher:
        raise HTTPException(status_code=404, detail="Course not found")
    
    teacher["id"] = str(teacher.pop("_id"))  
    return TeacherResponse(**teacher)



async def update_teacher(teacher_id:str, teacher:TeacherCreate) ->TeacherResponse:
    teacherid = ObjectId(teacher_id)
    updated_teacher = await teachers.update_one({"_id":teacherid}, {"$set": teacher.dict()})

    if updated_teacher.modified_count==0:
        raise HTTPException(status_code=404, detail="No data found")
    
    teacher_updated = await teachers.find_one({"_id": teacherid})
    teacher_updated["id"]= str(teacher_updated["_id"])
    return TeacherResponse(**teacher_updated)



async def delete_teacher(teacher_id:str):
    teacherid=ObjectId(teacher_id)
    delete_result = await teachers.delete_one({"_id":teacherid})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="teacher not found")

    return ("teacher deleted")

