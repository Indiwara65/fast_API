from fastapi import FastAPI
from enum import Enum

emojis = {"smiley_face":":-)",
          "winking_face":";-)",
          "surprised_face": ":-O",
          "sad_face" : ":-(",
          "cool_face":"B-)",
          "laughing_face" : "XD",
          "tongue_out" : "-P",
          "heart" : "<3",
          "thumbs_up" : "b(^_^)d",
          "shrug" : "¯\_(ツ)_/¯"}

emoji_Ids = {"0":"smiley_face",
             "1":"winking_face",
             "2":"surprised_face",
             "3":"sad_face",
             "4":"cool_face",
             "5":"laughing_face",
             "6":"tongue_out",
             "7":"heart",
             "8":"thumbs_up",
             "9":"shrug"}

app = FastAPI()               #fastAPI instance

@app.get("/",description="Deafult Path")                       #decorator               - specifies the HTTP method and path
async def root():                                                    #function/path_operation - operation to be performed once the path is called
    return "(づ｡◕‿‿◕｡)づ  𝐸𝓂𝑜𝒿𝒾  (✿◠‿◠)"

####### Order Matters #######
#When calling routes the routes declared first are called initally
#The function cool_face() is called rather than read_emoji() when path "emojies/cool_faces" is called as this path is defined first.
@app.get("/emojis/cool_faces")
async def cool_face():
    return f"{emojis['cool_face']} {emojis['cool_face']}"

####### Path Parameters #######
#path parameters/variables are used to get data from the user
#if type is not defined the default type is string

##Path Parameters without type
@app.get("/emojis/{emoji_name}")
async def read_emoji(emoji_name):
    print(f"emoji_name : {emoji_name}")
    print(f"type : {type(emoji_name)}")
    if emoji_name in emojis.keys():
        return emojis[emoji_name]
    else:
        return f"No emoji found {emojis['sad_face']}"
    
##Path Parameters with type
@app.get("/emoji_id/{emoji_Id}")
async def read_emoji_Id(emoji_Id:int):
    print(f"emoji_Id : {emoji_Id}")
    print(f"type : {type(emoji_Id)}")
    emoji_Id = str(emoji_Id)
    if emoji_Id in emoji_Ids.keys():
        emoji_name = emoji_Ids[emoji_Id]
        return emojis[emoji_name]
    else:
        return f"No emoji found {emojis['sad_face']}"
    
####### Predefined Values #######

class DefaultEmoji(str, Enum):
    smiley_face = "smiley_face"
    cool_face = "cool_face"
    heart = "heart"

class DefaultEmojiId(int, Enum):
    smiley_face = 0
    cool_face = 4
    heart = 7

@app.get("/default_emoji/{emoji_name}")
async def read_default_emoji(emoji_name:DefaultEmoji):
    return emojis[emoji_name.value]

@app.get("/default_emoji_id/{emoji_id}")
async def read_default_emoji_id(emoji_Id:DefaultEmojiId):
    #print(f"emoji Id : {emoji_Id.value}")
    return emoji_Ids[str(emoji_Id.value)]