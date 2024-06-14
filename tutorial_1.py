#Fast API Intialization, Path Parameters, Query Parameters
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

user_data = {
    'user0':{
        'name':'Jorge',
        'userId':'0121',
        'language':'python'
    },
    'user1':{
        'name':'Jimmy',
        'userId':'0122',
        'language':'python'
    },
    'user2':{
        'name':'Sam',
        'userId':'0123',
        'language':'java'
    },
    'user3':{
        'name':'',
        'userId':'0123',
        'language':'python'
    }
}

services = ['ML', 'Web Development', 'Data Analytics', 'Electronics']

@app.get("/")
async def root():
    # return type can be dict, list, str, int, etc...
    return {"message":"Hello World"}

##path parameters##
@app.get("/service/{service}")
async def service_check(service:int):
    if  service in services:
        return True
    else :
        return False

##order matters##
#if 'users/me' path was not defined first 'users/{user_id}' will always be choosen
@app.get("/users/me")
async def read_user_me():
    return user_data['user0']

@app.get("/users/{user_id}")
async def read_user(user_id:str):
    if user_id in user_data:
        return user_data[user_id]
    else:
        return {user_id : None}

##predefined values (ennumeration)##
#a set of predifined values for th path parameter
class Language(str, Enum):
    python = "python"
    java = "java"
    csharp = "csharp"

@app.get("/language/{language}")
async def language_check(language:Language):
    return {'language':language}

##query parameter##
#query parameters are used to define path parameters with default values
#if path parameters are not defined then they will be set automatically to the default values
#eg URL - hhtps://example.com/items/?skip=0&limit=10


@app.get("/add/")
async def addition(num1:int=0, num2:int=0):
    return {'addition':num1+num2}

#optional parameters
@app.get("/addto/")
async def addto(num1:int=0, num2:int | None = None):
    if num2:
        return num1 + num2
    else:
        return num1 + 10
    
