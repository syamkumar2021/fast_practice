from fastapi import FastAPI
from typing import Optional # to make any field 'optional' and pass the value as "None"
from pydantic import BaseModel # for validation

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello World"
    }

@app.get("/greet")
def greet():
    return {
        "message": "Hello Sam"
    }

@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int]=None):
    return {
        "message": f"Hello, {name} and you are {age} years old"
    }
# if I remove {name} in "/great/{name}" then it become query parameter(s)

@app.get("/greet1")
def greet_name(name: str, age: Optional[int]=None):
    return {
        "message": f"Hello, {name} and you are {age} years old"
    }

class Student(BaseModel):
    name: str
    age: int
    role: int

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "role": student.role
    }
