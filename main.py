from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 

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

class Item(BaseModel):
    name: str # 아무것도 안적으면 required가 됨
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int,item:Item, q:str | None = None):
    result = {"item_id":item_id, **item.dict()}

    if q:
        result.update({"q":q})
    return result