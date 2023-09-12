from enum import Enum
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "heeloo"}

@app.post("/")
async def postt():
    return {"ty":"ho"}

@app.put("/")
async def putt():
    return {"asdf":"sadf"}

@app.get("/items")
async def list_items():
    return {"message": "list items routes"}

@app.get("/items/{item_id}")
async def get_item(item_id):
    return {"item_id":item_id}

