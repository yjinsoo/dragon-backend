'''
Step 1: Instance 클래스를 만들고, state (BUILDING, RUNNING, DELETED) 필드를 넣습니다.

Step 2: 생성 API를 호출하면 비동기로 3초 뒤에 state를 RUNNING으로 바꿉니다.

Step 3: 삭제 API를 호출하면 아까처럼 DB와 Storage를 지우고 최종적으로 state를 DELETED로 바꿉니다.
'''

from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

class Instance:
  def __init__( self, name, state ):
    self.name = name
    self.state = state

async def delete_db():
  print("DB삭제 진행, 소요시간: 2초")
  await asyncio.sleep(2)
  print("DB삭제 완료")
  
async def delete_storage():
  print("Storage삭제 진행, 소요시간: 1초")
  await asyncio.sleep(1)
  print("Stroage삭제 완료")


@app.get("/create-instance")
async def create_instace(name: str):

@app.get("/delete-instace")
async def delete_instance():

