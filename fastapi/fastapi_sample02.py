'''
API 주소: /delete-project

입력 파라미터:
project_name: 삭제할 프로젝트 이름 (기본값: "temp-project")
force: 강제 삭제 여부 (타입: bool, 기본값: False)

내부 로직:
함수 내부에 async def delete_db()와 async def delete_storage()라는 중첩 함수를 정의하세요.
delete_db는 2초, delete_storage는 1초가 소요됩니다. (asyncio.sleep 사용)
만약 force가 True이면 두 함수를 동시에(gather) 실행하고, False이면 순차적으로(await 따로따로) 실행하세요.
결과 반환: 총 소요 시간과 함께 "삭제 완료" 메시지를 JSON으로 반환하세요.
'''

from fastapi import FastAPI
import asyncio, time

app = FastAPI()

class Project:
  def __init__(self, name, force):
    self.name = name
    self.force = force

async def delete_db():
  print("DB삭제 진행, 소요시간: 2초")
  await asyncio.sleep(2)
  print("DB삭제 완료")
  
async def delete_storage():
  print("Storage삭제 진행, 소요시간: 1초")
  await asyncio.sleep(1)
  print("Stroage삭제 완료")
  
@app.get("/delete-project")
async def delete_project(name: str = "temp-project", force: bool = False):
  start = time.time()
  target_project = Project(name,force)
  async_wether = 2

  tasks = [ delete_db(), delete_storage() ]
  print(f"Project: {target_project.name}을 삭제합니다. 강제여부: {target_project.force}")

  try:
    if target_project.force:
      async_wether = 1
      await asyncio.gather(*tasks)
    else:
      await delete_db()
      await delete_storage()
  except Exception as e:
    return { "error msg": f"{e}" }  

  end = time.time()

  return  {
    "message" : "project 삭제 완료",
    "Force" : f"{target_project.force}",
    "async_wether" : f"{async_wether}",
    "elapsed_time" : f"{ end - start }s"
  }
    
