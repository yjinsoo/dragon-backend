import asyncio
import httpx
import os
import platform
import time

# 1. [Class 활용] 서버 정보를 담는 클래스
class Server:
    def __init__(self, name, url):
        self.name = name
        self.url = url

# 2. [비동기 + 예외처리] 실제 체크 로직
async def check_server_status(client, server):
    start = time.time()
    try:
        # [미션 1] 비동기로 해당 server.url에 접속하세요 (timeout은 2초)
        response = await client.get(server.url, timeout=2.0)
        status = "✅ 정상" if response.status_code == 200 else "⚠️ 이상"
    except Exception as e:
        status = "🚨 접속 불가"
    
    end = time.time()
    return f"[{server.name}] 상태: {status} ({end-start:.2f}s)"

# 3. [OS 모듈 활용] 현재 내 컴퓨터 정보 가져오기
def get_system_info():
    # [미션 2] os 모듈이나 platform 모듈을 써서 현재 OS 이름과 프로세스 ID(PID)를 반환하세요
    os_name = platform.system()
    pid = os.getpid()
    return f"운영체제: {os_name} / 프로세스ID: {pid}"

async def main():
    # 체크할 서버 목록 (객체 생성)
    server_list = [
        Server("Google", "https://www.google.com"),
        Server("GitHub", "https://www.github.com"),
        Server("FakeServer", "https://this.is.fake.url")
    ]

    print(f"--- 모니터링 시작 ({get_system_info()}) ---")
    
    # [미션 3] httpx.AsyncClient를 열고 gather를 이용해 모든 서버를 '동시에' 체크하세요
    async with httpx.AsyncClient() as client:
        tasks = [check_server_status(client, s) for s in server_list]
        results = await asyncio.gather(*tasks)

    print("\n--- 리포트 결과 ---")
    for res in results:
        print(res)

if __name__ == "__main__":
    asyncio.run(main())
