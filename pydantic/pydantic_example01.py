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

@app.get("/get-instance/{name}")
async def get_instance(name: str):
    # 2. 메모리(딕셔너리)에서 이름으로 조회
    instance = instance_db.get(name)
    
    # 만약 없다면 404 에러를 뱉음 (인프라 엔지니어의 기본!)
    if not instance:
        raise HTTPException(status_code=404, detail="해당 이름의 인스턴스를 찾을 수 없습니다.")
    
    return instance

@app.get("/list-instances")
async def list_instances():
    # 3. 현재 메모리에 있는 모든 인스턴스 목록 반환
    return instance_db
