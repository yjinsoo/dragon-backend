import asyncio
import psutil
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

@app.get("/admin/monitor/cpu")
async def stream_cpu_status():
    # StreamingResponse에 생성기(Generator)를 담아서 리턴
    return StreamingResponse(monitor_cpu_usage(), media_type="text/plain")
