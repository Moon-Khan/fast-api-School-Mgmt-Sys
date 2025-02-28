from schemas import StudentCreate, StudentResponse
from fastapi import  HTTPException
from models import students
from bson import ObjectId
from typing import List


async def create_student(student:StudentCreate)->StudentResponse:
    stduentData=student.dict()
    result = await students.insert_one(stduentData)
    
    if not result.inserted_id:
        raise HTTPException (status_code=500, detail="Student not created")
    
    return StudentResponse(**stduentData, id=str(result.inserted_id))



async def get_all_students() ->List[StudentResponse]:
    stds=[] 

    async for std in students.find():
        std["id"]=str(std["_id"])
        stds.append(StudentResponse(**std))

    return stds



async def get_student(student_id: str)->StudentResponse:
    student = await students.find_one({"_id":ObjectId(student_id)})

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student["id"] = str(student.pop("_id"))  
    return StudentResponse(**student)  



async def update_student(student_id:str, student:StudentCreate)->StudentResponse:
    studentid=ObjectId(student_id)
    updated_student = await students.update_one({"_id":studentid}, {"$set":student.dict()})   

    if updated_student.modified_count==0:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student_updated = await students.find_one({"_id":studentid})
    student_updated["id"]= str(student_updated["_id"])
    return StudentResponse(**student_updated)



async def delete_student(student_id:str):
    studentid=ObjectId(student_id)
    delete_result = await students.delete_one({"_id":studentid})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="STUDENT not found")

    return ("student deleted")