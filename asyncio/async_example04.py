'''
3개의 사이트에 동시에 요청을 보내서, 가장 빨리 응답이 오는 사이트가 어디인지 찾아내는 도구를 만드세요.

[조건]

httpx.AsyncClient()를 사용하세요.
fetch_speed(name, url)라는 비동기 함수를 만듭니다.
함수 내부에서 time.time()을 이용해 응답에 걸린 시간을 계산하세요.
결과로 "{name} - {소요시간}초" 문자열을 반환(return)하세요.
main()에서 asyncio.gather를 사용해 구글, 네이버, 다음 3곳을 동시에 찌르세요.
'''

import asyncio
import httpx
import time

async def fetch_speed(client, name, url):
    start = time.time()
    # 1. 여기서 비동기로 url에 접속하세요 (await 사용)
    # 2. 소요 시간을 계산하세요
    return f"{name}: {duration:.4f}s"

async def main():
    urls = {
        "Google": "https://www.google.com",
        "Naver": "https://www.naver.com",
        "Daum": "https://www.daum.net"
    }
    
    
    async with httpx.AsyncClient() as client:
        # 3. 여기서 tasks 리스트를 만들고 gather로 실행하세요
        tasks = [fetch_speed(cllent,name,url) for name, url in urls.items()]
        results = await asyncio.gather(*tasks)

    for res in results:
        print(res)
        
asyncio.run(main())
