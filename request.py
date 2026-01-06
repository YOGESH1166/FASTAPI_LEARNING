from  fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional 

app=FastAPI()

class student(BaseModel):
  id : int
  name : str
  age: int
  degree : str


@app.post("/user")

def view(data : student):
  return {
    "message": "students details collected:",
    "data": data

  }

