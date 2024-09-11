from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
async def route():
    return "Hello"

########### Request Body ###########
#When data is sent from client to API a request body can be used.
#A request body is sent for every request but is not madetory.
#POST, DELETE or PATCH can be used to send data to the API
#Once a data model is created and added as a path parameter the client needs to send a request body with the mandotary fields as a JSON object
#The request body is read as JSON -> Convert data types(if needed) -> validate data
class Item(BaseModel):           #data model
    name:str
    description:str|None=None    #non mandotary filed (optional)
    price:float
    tax:float|None=None          #non mandatory filed

items = {"0":Item(
    name="Soda",
    description="Breverage",
    price=1.25,
    tax=0.02),
    "1":Item(
    name="Buger",
    description="Solid Food",
    price=2.25,
    tax=0.12),
    "2":Item(
    name="Fries",
    description="Solid Food",
    price=2.0,
    tax=0.10)
    }

@app.post("/items/")             #decclare it as a parameter
async def create_item(item:Item):
    last_item_Id = int(list(items.keys())[-1])
    item_Id = str(last_item_Id+1)
    items[item_Id] = item
    print(items)
    return item_Id

##Path parameter + request body
@app.put("/items/{item_Id}")
async def update_item(item_Id:str, item:Item):
    item_Ids = list(items.keys())
    if item_Id in item_Ids:
        items[item_Id] = item
        print(items[item_Id])
        return "Yes"
    else:
        return "NO"
    
##Path parameter + request body + query parameters
@app.put("/items/update_tax/{item_Id}")
async def update_item(item_Id:str, item:Item, tax_rate:float|None):
    item_Ids = list(items.keys())
    if item_Id in item_Ids:
        if tax_rate is not None:
            tax = item.price*tax_rate
            print(f"tax:{tax}")
            items[item_Id].tax = tax
        print(items[item_Id])
        return "Yes"
    else:
        return "NO"
        
