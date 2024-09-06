from fastapi import FastAPI, Cookie
from pydantic import BaseModel, Field
from typing import Annotated

app =FastAPI()

@app.get("/")
def Cook(st : Annotated[str , Cookie()]):
    return st