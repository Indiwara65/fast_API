from fastapi import FastAPI

posts = {"post1":"|",
         "post2":"|_",
         "post3":"|_|"}
app = FastAPI()

@app.get("/",description="Deafult Path")                       #decorator               - specifies the HTTP method and path
def root():                                                    #function/path_operation - operation to be performed once the path is called
    return {"message":"Hello World Updated"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/create_post")
def create_post(payload:dict):
    return {"message":"sucessfully created"}