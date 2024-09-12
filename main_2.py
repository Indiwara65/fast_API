from fastapi import FastAPI, Query, Path
from typing import Annotated

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

app = FastAPI()

#### String validations ####
@app.get("/emoji/")
async def read_emoji(q:str|None=None):     #query parameter is defined as a optional string query parameter
    if q is not None:
        if q in emojis.keys():
            return emojis[q]
        else:
            return f"{emojis['laughing_ face']} Unavailable {emojis['sad_face']}"
    else:
        return f"Cool {emojis['cool_face']}"
    
## Additional Validations for Strings
#max length
@app.get("/emoji/text/{emoji_name}")
async def emoji_plus_text(emoji_name:str, text:Annotated[str|None, Query(max_length=10)]):
    if emoji_name in emojis.keys():
        return f"{emojis[emoji_name]} {text}"
    else:
        return f"Unavailable {emojis['sad_face']}"
    
@app.get("/text/emoji/{emoji_name}")
async def text_plus_emoji(emoji_name:str, text:Annotated[str|None, Query(min_length=2, max_length=10)]):
    if emoji_name in emojis.keys():
        return f"{text} {emojis[emoji_name]}"
    else:
        return f"Unavailable {emojis['sad_face']}"

## Query Parameters List
@app.get("/emojis/")
async def emojis_return(q : Annotated[list[str]|None,Query(min_length=2,max_length=3)]=None):
    print(q)
    if q is None:
        return f"{emojis['cool_face']} {emojis['cool_face']}"
    text = ""
    print(emojis.keys())
    for emoji_name in q:
        print(emoji_name in emojis.keys())
        text = f"{text} {emojis[emoji_name]}" if emoji_name in emojis.keys() else text
    return text

##Path parameters validation
@app.get("/emoji/{emoji_Id}")
async def emoji_from_Id(emoji_Id:Annotated[int, Path(le=0, ge=9)]):     #le - less than or equal to, lt - less than, ge - greater than equal to, gt - grater than
    emoji_Id = str(emoji_Id)
    if emoji_Id in emoji_Ids.keys():
        emoji_name = emoji_Ids[emoji_Id]
        return emoji_name
    else:
        return f"Invalid Emoji Id {emojis['sad_face']}"
    

