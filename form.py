from fastapi import FastAPI,Form
app = FastAPI()

@app.post("/user")

def home(
  name:str =Form(...),
  age:int=Form(...),
  cls: str=Form(...)
):
  return{
    "status":"complete",
    "name": name,
    "age": age,
    "class": cls
  }