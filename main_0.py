from fastapi import FastAPI

posts = {"post1":"|",
         "post2":"|_",
         "post3":"|_|"}
app = FastAPI()               #fastAPI instance

@app.get("/",description="Deafult Path")                       #decorator               - specifies the HTTP method and path
async def root():                                                    #function/path_operation - operation to be performed once the path is called
    return {"message":"Hello World Updated"}

@app.get("/posts")
async def get_posts():
    return posts

