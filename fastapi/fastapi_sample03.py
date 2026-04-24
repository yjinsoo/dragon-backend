import httpx
from fastapi import FastAPI
import asyncio
import time

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
    
# 1. 외부 시스템에 보고하는 비동기 함수
async def notify_monitoring_center(project_name, user):
    # 가상의 모니터링 서버 주소입니다.
    url = "https://httpbin.org/post"  # 요청을 그대로 반사해주는 테스트용 사이트
    data = {"event": "DELETE_START", "project": project_name, "user": user}
    
    async with httpx.AsyncClient() as client:
        # 비동기로 외부 API에 POST 요청을 보냅니다.
        response = await client.post(url, json=data)
        res_data = response.json()
        if response.status_code == 200:
            print(f"📢 [Report] 모니터링 센터에 보고 완료: {project_name}")
            print(f"{res_data['json']}")
        return response.status_code

  
@app.get("/delete-project")
async def delete_project(name: str = "temp-project", force: bool = False):
  start = time.time()
  target_project = Project(name,force)
  async_wether = 2

  tasks = [ delete_db(), delete_storage() , notify_monitoring_center(target_project.name, "admin_jinsoo") ]
  print(f"Project: {target_project.name}을 삭제합니다. 강제여부: {target_project.force}")

  try:
    if target_project.force:
      async_wether = 1
      await asyncio.gather(*tasks)
    else:
      await asyncio.gather(delete_db(),notify_monitoring_center(target_project.name, "admin_jinsoo"))
      await asyncio.gather(delete_storage(),notify_monitoring_center(target_project.name, "admin_jinsoo"))
  except Exception as e:
    return { "error msg": f"{e}" }  

  end = time.time()

  return  {
    "message" : "project 삭제 완료 및 외부 보고 완료",
    "Force" : f"{target_project.force}",
    "async_wether" : f"{async_wether}",
    "elapsed_time" : f"{ end - start }s"
  }
