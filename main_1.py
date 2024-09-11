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

@app.post("/items/")             #decclare it as a parameter
async def create_item(item:Item):
    print(f"type:{type(item)}")
    print(f"name:{item.name}")
    print(f"desceiption:{item.description}")
    print(f"price:{item.price}")
    print(f"tax:{item.tax}")
    return item
