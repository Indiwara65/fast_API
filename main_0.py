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
    return emoji_Ids[str(emoji_Id.value)]

####### Query Parameters #######
#Query parameters are used afer a question and are not mandetory. 
#Query parameters can have default values unlike path parameters.
#Query parameters order doesn't matter


@app.get("/emoji_text/")
async def emoji_plus_text(text:str="Hi!", emoji_name:str="cool_face"):
    if emoji_name in emojis.keys():
        return f"{text} {emojis[emoji_name]}"
    else:
        return f"Emoji unavailable {emojis['sad_face']}"
    
##Optional query parameters
@app.get("/text_emoji/")
async def emoji_with_text(text:str|None=None, emoji_name:str='cool_face'):
    if text is not None and emoji_name in emojis.keys():
        text =  f"{text} {emojis[emoji_name]}"
    elif emoji_name in emojis.keys():
        text =  f"{emojis[emoji_name]}"
    else:
        text = f"Emoji unavailable {emojis['sad_face']}"
    return text

##Bool type query parameters
#query parameter value can be set to 1, True, true, on or yes which will be converted to python boolean
@app.get("/reverse_emoji/{emoji_name}")
async def emoji_reverse(emoji_name:str, reverse:bool=False):
    if emoji_name in emojis.keys():
        emoji = emojis[emoji_name]
        text = emoji if not reverse else emoji[::-1]
    else:
        emoji = emojis["sad_face"]
        text = f"{emoji} emoji unavailable {emoji[::-1]}"
    return text
##Required Query Parameters
#if a query parameter does not have a default value the the query parameter becomes mandetory
