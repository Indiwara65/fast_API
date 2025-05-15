from typing import Annotated, List
from fastapi import FastAPI, Body, Query
from pydantic import BaseModel, Field

class Item(BaseModel):
    name : str=Field(max_length=10)
    description : str|None=Field(None,max_length=50)
    price:float
    tax_rate:float=Field(ge=0,lt=1)

class Order(BaseModel):
    order_Id : int
    cost:float
    taxes:float
    total:float

app = FastAPI()

@app.get("/")
async def root():
    return "Price Listings"

## Response Model ##
#Method 1
@app.put("/items/total")
async def total(items:Annotated[List[Item], Body()], order_Id:Annotated[int, Query()]) -> Order:
    tot_price = 0
    tot_tax = 0
    for item in items:
        tot_price += item.price
        tot_tax += item.price*item.tax_rate
    order = Order(order_Id=order_Id, cost=tot_price, taxes=tot_tax, total=tot_price+tot_tax)
    return order
#Method 2
#response_model - define the data structure of the response
#response_model_exclude - exclude certain feilds of the data structure
#response_model_include - include certain feilds of the data structue
#status_code - can be used to set the http status code manually 
@app.put("/item/price", response_model=Order, response_model_exclude={"cost"}, response_model_include={"total"})
async def total_price(items:Annotated[List[Item], Body()], order_Id:Annotated[int, Query()]):
    tot_price = 0
    tot_tax = 0
    for item in items: 
        tot_price += item.price
        tot_tax += item.price*item.tax_rate
    order = Order(order_Id=order_Id, cost=tot_price, taxes=tot_tax, total=tot_price+tot_tax)
    return order


