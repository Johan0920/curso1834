from fastapi import APIRouter
from config.db import conn
from schemas.student_entity import studentEntity, studentsEntity
from models.student import Student
from bson import ObjectId

student = APIRouter()

@student.get('/students')
def get_all_student():
    return studentsEntity(conn.MTIC.estudiantes.find())

@student.post("/students")
def create_student(estudiante:Student):
    new_student= dict(estudiante)
    id = conn.MTIC.estudiantes.insert_one(new_student).inserted_id
    return f"El estudiante se ha creado {id}"

@student.get("/students/{id}")
def get_student(id:str):
    return studentEntity(conn.MTIC.estudiantes.find_one({"_id":ObjectId(id)}))

@student.delete("/students/{id}")
def delete_student(id:str):
    conn.MTIC.estudiantes.find_one_and_delete({"_id":ObjectId(id)})
    return "Estudiante eliminado"

@student.put("/students/{id}")
def update_student(id:str, stu:Student):
    conn.MTIC.estudiantes.find_one_and_update({"_id":ObjectId(id)},{"$set":dict(stu)})
    return studentEntity(conn.MTIC.estudiantes.find_one({"_id":ObjectId(id)}))
