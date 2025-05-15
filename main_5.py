from enum import Enum
from fastapi import FastAPI

class ChannelName(str, Enum):
    Cleet = "Cleetus McFarland"
    JH = "JH Diesel & 4x4"
    Matt = "Matts Offroad Recovery"

app = FastAPI()
names = {'1':"JH","2":"Cleet","3":"JackStand"}

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/main")
def main_path():
    return {"message":"This is the main path"}

@app.get("/who/name/{name}")
def who(name:str):
    if name.lower()=='jh':
        return {"message":"JH Who"}
    else:
        return {"message":name}  
    
@app.get("/who/id/{name_id}")
def who(name_id:int):
    name = names.get(str(name_id))
    print(name)
    if name is None:
        return {"message":"no entry"}
    elif name.lower() == 'jh':
        return {'message':"JH who"}
    else:
        return {"message":name}
    
@app.get("/channel/{channel_name}")
def channelName(channel_name:ChannelName):
    if channel_name==ChannelName.Cleet:
        owner = "Garret Mitchel"
    elif channel_name==ChannelName.JH:
        owner = "Justin hilbilly"
    elif channel_name==ChannelName.Matt:
        owner = "Matt Westlin"
    else:
        owner = "Not defined"
    return {'owner':owner}

##Querry Parameters
@app.get("/message/")
def hello(message:str):
    return {"message":message}

@app.get("/default/")
def default_message(message:str="Hello World", message_type:str=None):
    if message_type:
        return {"message":message,"message_type":message_type}
    else:
        return {"message":message}
    
#required query parameters
@app.get("/required/")
def required_message(message:str):
    return {'messsage':message}

#both path and query parameter
@app.get("/path/{channel_name}/owner/{owner}")
def path_query(channel_name:ChannelName,owner:str,rating:int):
    return {'channel_name':channel_name,'owner':owner,'rating':'good' if rating>3 else 'bad'}
