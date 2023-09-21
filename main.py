from enum import Enum
from fastapi import FastAPI, Query,Path,Body
from pydantic import BaseModel
from typing import Optional 

app = FastAPI()

# Part 7 Body Multiple parameters
class Item(BaseModel):
    name: str
    description: str | None = None
    price : float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None



@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item ot get", ge=0,le=150),
    q: str | None = None,
    item : Item | None = None,
    user:User,
    importance : int = Body(...)
):
    results ={"item_id": item_id}
    if q:
        results.update({"q": q})
    if item: 
        results.update({"item":item})
    if user:
        results.update({"user":user})
    if importance:
        results.update("importance",importance)

    return results











# @app.get("/")
# async def root():
#     return {"message": "heeloo"}

# @app.post("/")
# async def postt():
#     return {"ty":"ho"}

# @app.put("/")
# async def putt():
#     return {"asdf":"sadf"}

# @app.get("/items")
# async def list_items():
#     return {"message": "list items routes"}

# @app.get("/items/{item_id}")
# async def get_item(item_id):
#     return {"item_id":item_id}

# class Item(BaseModel):
#     name: str # 아무것도 안적으면 required가 됨
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.post("/items")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item_with_put(item_id: int,item:Item, q:str | None = None):
#     result = {"item_id":item_id, **item.dict()}

#     if q:
#         result.update({"q":q})
#     return result

# @app.get("/items")
# async def read_items(q: str | None = Query(None,min_length=3,max_length=10)):
#     results = {"items" : [{"item_id":"Foo"},{"item_id":"Bar"}]}
#     if q: 
#         results.update({"q":q})
#     return results

# @app.get('/items_hidden')
# async def hidden_query_route(hidden_query: str | None = Query(None, include_in_schema=False)  ):
#     if hidden_query:
#         return {"hidden_query": hidden_query}
#     return {"hidden_query": "Not found"}

# @app.get("/items_validation/{item_id}")
# async def read_items_validation(
#     item_id: int = Path(..., title="The ID of the item to get"), q:str | None = Query(None,alias='item-query'),):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results

