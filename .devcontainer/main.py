from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
import os

app = FastAPI()

# MongoDB connection
client = MongoClient("mongodb://mongodb:27017/")
db = client["template_db"]
users = db["users"]

class User(BaseModel):
    name: str
    email: str
    role: str = "user"

@app.get("/")
def read_root():
    return {"message": "MongoDB + Python in Codespaces!"}

@app.post("/users/", status_code=201)
def create_user(user: User):
    if users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    users.insert_one(user.dict())
    return {"message": "User created successfully"}

@app.get("/users/")
def read_users():
    return list(users.find({}, {"_id": 0}))

@app.get("/users/{email}")
def read_user(email: str):
    if (user := users.find_one({"email": email}, {"_id": 0})) is not None:
        return user
    raise HTTPException(status_code=404, detail="User not found")