from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import asyncio

app=FastAPI()



class User(BaseModel):
  name: str
  age: int = Field(ge=0, le=100)


@app.get("/create_user")



