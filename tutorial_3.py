#Validations - Path, Query & Body
from fastapi import FastAPI, Query, Path, Body
from pydantic import BaseModel, Field
from enum import Enum
from typing import Annotated

app = FastAPI()

@app.get("/")
def root():
    return {'message':"HelloWorld"}

##Query Parameter Validation##
#
@app.get("/add/")
def addition(num1:int, num2:int, num3:int | None = None):
    #num3 can ither be int or None and the default dtype is None and default value is None
    num3 = num3 if num3 else 0
    value = num1 + num2 + num3
    return {'value':value}
#min max length
@app.get("/string/")
def strvalid(s : Annotated[str, Query(max_length=5, min_length=2)]):
    return {'string':s}
#alias
@app.get("/strings/")
def strsvalid(string1: Annotated[str, Query(max_length=5,min_len=2, alias="s1")],
              string2: Annotated[str, Query(max_len=5, min_len=3, alias="s2")]):
    return {'string1':string2, 'string2':string1}
#metadata - title, description, example

##Path Parameter Validation##
#similar to query parameters
#numerical validations -
# ge-greater than equal, le-less than equal, gt-grater than , lt-less than
@app.get("/number/{num}")
def number(num : Annotated[int, Path(title='Integer NBumber', ge=0, lt=5)]):
    return {'number':num} 

##Body Validation##

# Body() can be used to validate the data structure
class CarInfo(BaseModel):
    name : str = Field(
        description="driver name",
        max_length=10,
        min_length=3
    )
    track_time : float =Field(
        gt = 0
    )
    car : str = Field(
        desctiption = "car mode",
        example = "Mustang"
    )
    drag_time : float = Field(
        gt = 0,
        le = 20
    )
@app.post("/carinfo/")
def valbody(carinfo : Annotated[CarInfo, Body()]):
    return carinfo

