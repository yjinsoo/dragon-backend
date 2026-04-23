'''
[조건]
check_db_connection()이라는 비동기 함수를 만듭니다.
이 함수는 실행될 때마다 await asyncio.sleep(0.5)를 합니다.
for 루프를 사용해 최대 3번 반복하며 접속을 시도하세요.
만약 접속에 실패하면(에러 가정), "재시도 중..."을 출력하고 다시 시도하세요.
마지막 3번째까지 실패하면 "최종 실패"를 출력하세요.

'''

import time,asyncio,httpx


async def check_db_connection(client, name, url):
  await asyncio.sleep(0.5)
  for i in range



async def main():
  services = {
        "AUTH-API": "https://jsonplaceholder.typicode.com/posts/1",
        "ORDER-API": "https://jsonplaceholder.typicode.com/posts/2",
        "PAY-API": "https://jsonplaceholder.typicode.com/posts/3",
        "INVENTORY-API": "https://invalid-url-test.com" # 에러 테스트용
  }

  async with httpx.AsyncClient() as client:
    tasks = [check_db_connection(client, name, url) for name, url in services.time()]
    await asyncio.gather{*tasks)

                         
asyncio.run(main())

    
    
