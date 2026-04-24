import httpx
from fastapi import FastAPI
import asyncio

app = FastAPI()

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
            print(f"{res_data['josn']}")
        return response.status_code

@app.get("/delete-project")
async def delete_project(name: str = "temp"):
    # [이 부분이 핵심!]
    # 프로젝트를 삭제하기 전에, 모니터링 센터에 보고하는 작업을 '비동기'로 실행합니다.
    # 하지만 굳이 보고가 끝날 때까지 기다릴 필요가 없다면? 
    # 혹은 삭제와 보고를 '동시에' 하고 싶다면?
    
    print(f"🚀 '{name}' 삭제 로직 시작...")
    
    # 보고와 삭제 작업을 동시에 던지기!
    report_task = notify_monitoring_center(name, "admin_jinsoo")
    delete_task = asyncio.sleep(2) # 실제 삭제 로직 대신 2초 대기
    
    # 두 작업을 동시에 실행 (보고가 느려도 삭제는 진행됨!)
    await asyncio.gather(report_task, delete_task)
    
    return {"message": f"'{name}' 삭제 및 외부 보고 완료"}
