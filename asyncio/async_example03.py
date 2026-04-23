import asyncio
import httpx
import time

async def check_service(client, name, url):
    try:
        # 접속 시도 (타임아웃 2초 설정)
        response = await client.get(url, timeout=2.0)
        status = "✅ UP" if response.status_code == 200 else f"❌ DOWN({response.status_code})"
    except Exception:
        status = "🚫 ERROR (Connection Failed)"
    
    print(f"[{name}] 상태 확인 중...")
    return f"{name}: {status}"

async def main():
    services = {
        "AUTH-API": "https://jsonplaceholder.typicode.com/posts/1",
        "ORDER-API": "https://jsonplaceholder.typicode.com/posts/2",
        "PAY-API": "https://jsonplaceholder.typicode.com/posts/3",
        "INVENTORY-API": "https://invalid-url-test.com" # 에러 테스트용
    }

    start = time.time()
    
    # 하나의 클라이언트를 공유해서 사용 (고수의 방식!)
    async with httpx.AsyncClient() as client:
        # 딕셔너리를 돌며 예약권(tasks) 생성
        tasks = [check_service(client, name, url) for name, url in services.items()]
        
        # 동시에 실행하고 결과 수집
        results = await asyncio.gather(*tasks)

    print("\n--- 점검 결과 보고서 ---")
    for res in results:
        print(res)
    
    print(f"\n총 점검 소요 시간: {time.time() - start:.2f}초")

if __name__ == "__main__":
    asyncio.run(main())
