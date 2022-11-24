from pydantic import BaseModel

class Student(BaseModel):
    name:str
    lastname:str
    clave:str