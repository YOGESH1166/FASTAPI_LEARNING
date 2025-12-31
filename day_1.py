from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
  return {"message":"hi! yogesh this your first program "}