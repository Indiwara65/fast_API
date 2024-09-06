##Path Parameters 
#path parameters or variables are used to take inputs to path operators from the user
#path parameters can be set to have specific type enumerations

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "HelloWorld"

#datatype not specified path variable
@app.get("/var_1/{var}")
def read_var1(var):
    return {"var":var,"var_type":str(type(var))}

#datatype specified
@app.get("/var_2/{var}")
def read_var2(var:int):
    return {"var":var, "var_type":str(type(var))}