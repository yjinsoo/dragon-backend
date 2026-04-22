import asyncio
import httpx  # 비동기 전용 requests 같은 놈
import time

async def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    async with httpx.AsyncClient() as client:
        print(f"📦 Post {post_id} 요청 중...")
        response = await client.get(url)
        return response.json()['title']

async def main():
    start = time.time()
    
    # 1번부터 10번 포스트까지 리스트로 작업을 만듭니다.
    tasks = [fetch_post(i) for i in range(1, 11)]
    
    # 동시에 던지기!
    results = await asyncio.gather(*tasks)
    
    for i, title in enumerate(results, 1):
        print(f"[{i}] {title}")
        
    end = time.time()
    print(f"🚀 10개 API 동시 요청 총 소요 시간: {end - start:.2f}초")

if __name__ == "__main__":
    asyncio.run(main())
