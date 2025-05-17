from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class Item(BaseModel):
    name:str
    description:str | None = None
    price:float
    tax:float

class User(BaseModel):
    name:str
    employee_ID:int

@app.post("/create_item/")
def create_item(item:Item):
    return item

#request body plus path parameters
@app.put("/update_item/{item_id}")
def update_item(item_id:int,item:Item):
    return {"message":"Successful","item":item}

#request body plus path plus query
@app.put("/search_item/{item_id}")
def search_item(item_id:int,item:Item,q:bool=False):
    return {"item_id":item_id, "item":item, "state":q}

#request body + request body
@app.put("/add_item/")
def add_item(item:Item,user:User,new:bool=True):
    return {"item_name":item.name,"employee":user.name}