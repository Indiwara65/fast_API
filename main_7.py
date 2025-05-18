from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum
import random

#data classes
class User(BaseModel):
    employee_ID:int
    name:str

class Item(BaseModel):
    name:str
    description:str|None = None
    unit_price:float
    tax_percentage:float = Field(default=0.1,ge=0,le=1, description="Tax percentage should be a number in between 0 and 1. For example if tax percentage is 10% the value must be 0.1")

#enumerations
class ItemFileds(str, Enum):
    field_1 = 'name'
    filed_2 = 'description'
    field_3 = 'unit_price'
    filed_4 = 'tax_percentage'


class updateBody(BaseModel):
    field:ItemFileds
    str_value:str|None=None
    float_value:float|None=None

app = FastAPI()

@app.get("/")
def root():
    return {"status":"Ok"}

@app.get("/read/{item_id}/")
def read(item_id:int,price_only:bool=False):
    return{"item_id":item_id}

@app.post("/new/item/")
def add(item:Item,user:User):
    return{"item_id":random.randint(1,1000),"status":True}

@app.put("/update/{item_id}")
def update(item_id:int,update:updateBody):
    return{"item_id":item_id,"status":True}