from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
import asyncio

app = FastAPI()

'''
1. 가상의 데이터베이스 (In-memory DB)
서버가 커져있는 동안만 유지
'''
instance_db = {}

class InstanceCreate(BaseModel):
  name: str
  cpu: Literal[1,2,4,8]
  state: str = "BUILDING"

@app.post("/create-instance")
async def create_instance(instance: InstanceCreate):
  # 중복체크 : 이미 같은 이름의 인스턴스가 있다면?
  if instance.name in instance_db:
    raise HTTPException(status_code=400, detail="이미 존재하는 인스턴스 이름")
  instance_db[instance.name] = instance


  await asyncio.sleep(3)

  instance.state = "RUNNING"
  print(f"[{instance.name}] 생성 완료 및 RUNNING 상태 전환")
    
  return instance
