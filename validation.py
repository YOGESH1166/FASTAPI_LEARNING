from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()



class Customer(BaseModel):
  customer_id : int
  customer_name: str = Field(max_length=10,min_length=1,pattern="^[a-zA-Z]+$")
  customer_age: int = Field(gt=0,lt=100)


@app.post("/display")

def display(data: Customer):
  return{"message":"customer details",
           "data": data}