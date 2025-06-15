#Response Types
import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, FileResponse, StreamingResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
app = FastAPI()

##mounting a folder to routes
app.mount("/media", StaticFiles(directory="media"), name="media")

@app.get("/")
async def root():
    return {}

##HTML Response
@app.get("/html")
async def html_response():
    html_content = """
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1>Hello, FastAPI with HTML!</h1>
            <p>This is an HTML response.</p>
        </body>
    </html>
    """
    headers = {"header":"demo header"}
    return HTMLResponse(content=html_content, status_code=200, headers=headers)

##JSON Response
@app.get("/json")
async def json_response():
    json_content = {"content":"this is a json response"}
    return JSONResponse(content=json_content, status_code=201)

##PlainTextResponse
@app.get("/text")
async def text_response():
    text = "This is a text response"
    return PlainTextResponse(content=text)

##File Response
@app.get("/file")
async def file_response():
    file_path = "media/map.jpg"
    return FileResponse(
        path=file_path
    )

##Streaming Response
async def async_stream():
    for i in range(5):
        yield f"data chunk {i}\n"
        await asyncio.sleep(1)
@app.get("/stream")
async def stream_response():
    return StreamingResponse(content=async_stream(), media_type="text/plain")

##Redirect Response
@app.get("/redirect")
async def redirect():
    return RedirectResponse(url="/html")

#DIRECT METHOD
##HTML Response
@app.get("/HTML", response_class=HTMLResponse)
async def HTML_Response():
    html_content = """
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <h1>Hello, FastAPI with HTML!</h1>
            <p>This is an HTML response.</p>
        </body>
    </html>
    """
    return html_content

##JSON Response
@app.get("/JSON", response_class=JSONResponse, status_code=201)
async def JSON_Response():
    json_content = {"content":"this is a json response"}
    return json_content

##Plain text response
@app.get("/TEXT", response_class=PlainTextResponse)
async def TEXT_Response():
    text = "Hello! this is a text response"
    return text

##