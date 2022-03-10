from fastapi import APIRouter

from models.students_model import Students
from config.database import students_collection

from schemas.students_schema import students_serializer, student_serializer
from bson import ObjectId

students_api_router = APIRouter()

# retrieve
@students_api_router.get("/students/")
async def get_students():
    students = students_serializer(students_collection.find())
    return students

@students_api_router.get("/students/{id}")
async def get_students(id: str):
    return students_serializer(students_collection.find_one({"_id": ObjectId(id)}))


# post
@students_api_router.post("/students/")
async def create_students(student: Students):
    _id = students_collection.insert_one(dict(student))
    return students_serializer(students_collection.find({"_id": _id.inserted_id}))


# update
@students_api_router.put("/students/{id}")
async def update_students(id: str, student: Students):
    students_collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(student)
    })
    return students_serializer(students_collection.find({"_id": ObjectId(id)}))

# delete
@students_api_router.delete("/students/{id}")
async def delete_students(id: str):
    students_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}