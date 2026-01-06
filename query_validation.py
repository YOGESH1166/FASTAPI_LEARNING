from fastapi import FastAPI,Query
app = FastAPI()

st=[ {"name":"steve","age":35},
          {"name":"jacek","age":27},
          {"name":"dustin","age":15} ,    
          ]

@app.get("/user")
def view(
  name: str = Query(min_length=3,max_length=10,pattern="^[a-zA-Z]+$")):
  for s in st:
    if s["name"]==name:
      return s
    else:
      return{"message":"student not found:"}