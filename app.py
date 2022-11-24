from fastapi import FastAPI
from routes.student_route import student

app=FastAPI()

app.include_router(student)