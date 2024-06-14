#Request Body
#Request Body + Path Parameters
#Request Body + Path Parameters + Query Parameters
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

class operation(str, Enum):
    ADD = "add"
    SUB = "sub"
    MUL = "mul"
    DIV = "div"

class Calculation(BaseModel):
    op : operation='div' 
    num1 : float=10
    num2 : float=10

class Values(BaseModel):
    num1 : int
    num2 : int

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World"}
##Request Body##
#A request body can be used to convey data from client to server or vice versa
#A request body is sent as a json payload

@app.post("/arithmatic/")
async def calculation (calculation:Calculation):
    op = calculation.op.value
    num1 = calculation.num1
    num2 = calculation.num2
    calculation = dict(calculation)

    if op == 'add':
        calculation['value'] = num1 + num2
    elif op == 'sub':
        calculation['value'] = num1 - num2
    elif op == 'mul':
        calculation['value'] = num1 * num2
    elif op == 'div':
        if num2 != 0:
            calculation['value'] = num1 / num2
        else:
            calculation['value'] = num1
    else:
        calculation['value'] = None
    return calculation

##POST without Request Body#
#Here POST method used in conjugation with query parameters
@app.post("/arith/")
async def calc(op:operation='add',num1:float=10, num2:float=10):
    op = op.value
    calculation = {
        'op' : op,
        'num1' : num1,
        'num2' : num2
    }

    if op == 'add':
        calculation['value'] = num1 + num2
    elif op == 'sub':
        calculation['value'] = num1 - num2
    elif op == 'mul':
        calculation['value'] = num1 * num2
    elif op == 'div':
        if num2 != 0:
            calculation['value'] = num1 / num2
        else:
            calculation['value'] = num1
    else:
        calculation['value'] = None
    return calculation


#Request Body with Path Parameters
@app.post("/math/{op}")
async def math(op:operation, values:Values):
    num1 = values.num1
    num2 = values.num2
    op = op.value
    calculation = {
        'op' : op,
        'num1' : num1,
        'num2' : num2
    }

    if op == 'add':
        calculation['value'] = num1 + num2
    elif op == 'sub':
        calculation['value'] = num1 - num2
    elif op == 'mul':
        calculation['value'] = num1 * num2
    elif op == 'div':
        if num2 != 0:
            calculation['value'] = num1 / num2
        else:
            calculation['value'] = num1
    else:
        calculation['value'] = None
    return calculation


#Request Body + Path Parameters + Query Parameters
@app.post("/mathplus/{op}")
async def mathplus(op:operation, values:Values, num3:int | None = None):
    num1 = values.num1
    num2 = values.num2
    op = op.value
    calculation = {
        'op' : op,
        'num1' : num1,
        'num2' : num2,
        'num3' : num3
    }
    if not num3:
        num3 = 1 if (op == 'div' or op == 'mul') else 0
        del calculation['num3']
    
    if op == 'add':
        calculation['value'] = num1 + num2 + num3
    elif op == 'sub':
        calculation['value'] = num1 - num2 - num3
    elif op == 'mul':
        calculation['value'] = num1 * num2 * num3
    elif op == 'div':
        if num2 != 0 or num3 != 0:
            calculation['value'] = num1 / num2 / num3
        else:
            calculation['value'] = num1
    else:
        calculation['value'] = None
    return calculation