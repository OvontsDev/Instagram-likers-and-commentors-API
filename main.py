################################################################ FastAPI ##############################################################

# importing the required libraries
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List, Optional

### creating fastAPI instance
app = FastAPI()

### connecting to mongodb database
client = MongoClient("mongodb+srv://ovontsdev:nx7LgnXLduzKu5A@ovonts0.5ymhm.mongodb.net/development")
db = client['User']
LIKERS_COLLECTION = db['Likers']
COMMENTOR_COLLECTION = db['Commentors']

# Likers class defined in Pydantic
class Likers(BaseModel):
  username: str
  instagramID:Optional[int] = None
  postId:str
  fbid : Optional[int] = None
# Commentors class defined in Pydantic
class Commentors(BaseModel):
  username: str
  instagramID:Optional[int] = None
  postId:str
  fbid : Optional[int] = None


# Instantiate the FastAPI
@app.get("/")
def get_status():
    """Get status of messaging server."""
    return {"status": "running"}

# get the list of users who all likes the post 
@app.get("/likers/postId/{postId}",response_model=List[Likers])
async def get_user(postId:str):
  user_document = LIKERS_COLLECTION.find({"postId":postId})
  users = []
  for user in user_document:
    users.append(Likers(**user))
  return users

#get the user by instagramID
@app.get("/likers/instagramID/{instagramID}",response_model=Likers)
async def get_user_by_instaId(instagramID:int):
  user_document = LIKERS_COLLECTION.find_one({"instagramID":instagramID})
  return user_document

#get the user by username
@app.get("/likers/username/{username}",response_model=Likers)
async def get_user_by_username(username:str):
  user_document = LIKERS_COLLECTION.find_one({"username":username})
  return user_document




# get the list of users who all commented the post 
@app.get("/commentors/postId/{postId}",response_model=List[Commentors])
async def get_user(postId:str):
  user_document = COMMENTOR_COLLECTION.find({"postId":postId})
  users = []
  for user in user_document:
    users.append(Commentors(**user))
  return users

#get the user by instagramID
@app.get("/commentors/instagramID/{instagramID}",response_model=Commentors)
async def get_user_by_instaId(instagramID:int):
  user_document = COMMENTOR_COLLECTION.find_one({"instagramID":instagramID})
  return user_document

#get the user by username
@app.get("/commentors/username/{username}",response_model=Commentors)
async def get_user_by_username(username:str):
  user_document = COMMENTOR_COLLECTION.find_one({"username":username})
  return user_document
