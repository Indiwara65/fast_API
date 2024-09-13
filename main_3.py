import pprint
from typing import Annotated
from fastapi import FastAPI, Query, Path , Body, Cookie
from pydantic import BaseModel, Field

##Field can be used to define metadata inside a request body defined using BaseModel##
class Item(BaseModel):
    name:str
    description:str|None=Field(default=None, max_length=50, title="Small Description About the Item")
    price:float=Field(gt=0,lt=100)
    tax:float=Field(ge=0,le=100,default=0)

items = {
    "0":Item(name="Soda",description="Breverage",price=1.25,tax=0.02),
    "1":Item(name="Buger",description="Solid Food",price=2.25,tax=0.12),
    "2":Item(name="Fries",description="Solid Food",price=2.0,tax=0.10)
    }

app = FastAPI()

@app.get("/")
async def root():
    return "Price Listings"

##Single Body Parameter
@app.post("/item/update")
async def item_update(item:Item):
    item_Id = str(int(list(items.keys())[-1]) + 1)
    items[item_Id] = item
    pprint.pprint(items)
    return item_Id

##Multiple Body Parameters
@app.put("/item/add")
async def item_add(item_1:Item, item_2:Item):
    items_price = item_1.price + item_2.price
    items_tax = item_2.tax + item_2.tax
    items_tot = items_price + items_tax
    return {"price":items_price, "tax":items_tax, "tot":items_tot}

##Receive other variables in the request body
@app.put("/items/discount")
async def item_discount(item_1:Item, item_2:Item, dis_rate:Annotated[float, Body(ge=0,le=0.5)]):
    total = item_1.price + item_2.price + item_1.tax + item_2.tax
    discount = total*dis_rate
    return {"total":total, "discount":discount}

##Receive as JSON
@app.put("/items/tax_rate")
async def cal_tax_rate(item:Annotated[Item, Body(embed=True)]):
    return round(item.tax/item.price, 2)

########## Cookies ##########
@app.put("/items/description/")
async def get_description(item_id:Annotated[str, Cookie()]):
    print(f"Cookie:{item_id}")
    print(type(item_id))
    if item_id in items.keys():
        description = items[item_id].description
    else:
        description = "Invalid Id"
    return description