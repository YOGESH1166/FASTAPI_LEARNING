from fastapi import FastAPI
app = FastAPI()
@app.get("/user/{username}")

def get_user(username: str):
  return {"ENTER YOUR NAME IN URL":username}