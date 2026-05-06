'''
📝 미션: "서버 하드디스크 용량 실시간 중계"인프라 관리자용 API를 만든다고 가정합시다. 
서버의 특정 경로(/ 등)의 남은 용량을 5번만 스트리밍으로 쏴주고 종료되는 API를 만들어보세요.
💡 힌트 1: "몇 번 보낼 것인가?"while True 대신, range()를 사용해서 루프 횟수를 제한해 보세요.루프 안에서 yield를 사용해 데이터를 내보내야 합니다.
💡 힌트 2: "디스크 정보는 어떻게 가져오나?"파이썬 내장 라이브러리인 shutil을 사용하면 편리합니다.total, used, free = shutil.disk_usage("/") 명령어를 쓰면 바이트(Byte) 단위로 용량이 나옵니다. (GB 단위로 바꾸려면 $1024^3$으로 나누면 되겠죠?)
💡 힌트 3: "시간 지연"너무 빨리 지나가면 스트리밍 느낌이 안 나니까, await asyncio.sleep(2) 정도로 간격을 줘보세요.
'''
import asyncio
import psutil
import shutil
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from datetime import datetime

app = FastAPI()

async def monitor_cpu_usage():
    """
    서버의 CPU 사용량을 1초마다 측정하여 스트리밍하는 Generator
    """
    while True:
        # 1. 실제 서버의 CPU 사용률 측정
        cpu_percent = psutil.cpu_percent(interval=None)
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # 2. 클라이언트에게 보낼 데이터 포맷팅
        data = f"[{timestamp}] Current CPU Usage: {cpu_percent}%\n"
        
        # 3. 데이터 한 줄을 즉시 방출 (함수는 여기서 일시 정지)
        yield data
        
        # 4. 1초 동안 비동기 대기 (이동안 서버는 다른 작업을 처리 가능)
        await asyncio.sleep(1)

async def monitor_disk_usage():
    for i in range(1,6,1):
        disk = shutil.disk_usage("/")
        timestamp = datetime.now().strftime("%H:%M:%S")

        data = f"[{timestamp}] Current Disk Usage: {disk}bytes\n"
        yield data

        await asyncio.sleep(3)

@app.get("/admin/monitor/cpu")
async def stream_cpu_status():
    # StreamingResponse에 생성기(Generator)를 담아서 리턴
    return StreamingResponse(monitor_cpu_usage(), media_type="text/plain")


@app.get("/admin/monitor/disk")
async def stream_disk_status():
    return StreamingResponse(monitor_disk_usage(), media_type="text/plain")
