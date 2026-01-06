from fastapi import FastAPI
app = FastAPI()
student = [
            {"name":"yogesh","age":22,"degree":"MCA"},
            {"name":"naruto","age":21,"degree":"bca"},
            {"name":"minato","age":25,"degree":"bcom"},
            {"name":"itachi","age":27,"degree":"b.tech"}
]
@app.get("/user")

def get_user(name:str):
  for s in student:
    if s["name"]==name:
      return s