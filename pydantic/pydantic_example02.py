from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import asyncio

user_list_db = {}
app=FastAPI()

class User(BaseModel):
  name: str
  age: int = Field(ge=0, le=100)


@app.post("/create-user")
async def create_user(user: User):
  if user.name in user_list_db:
    raise HTTPException(status_code=400, detail="이미 존재하는 USER")
  user_list_db[user.name] = user


@app.get("/check-user/{username}")
async def check_user(username: str):
  user = user_list_db.get(username)

  if not user:
    raise HTTPException(status_code=404, detail="해당 USER를 찾을 수없음")

  return user

@app.get("/list-user")
async def user_list():
  return user_list_db



