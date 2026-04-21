'''
우리가 지금까지 짠 코드는 모두 동기(Synchronous) 방식이었습니다.

동기: 코드가 위에서 아래로 한 줄씩 실행됩니다. 한 줄이 끝날 때까지 다음 줄은 '대기'합니다.
  예: requests.get()으로 데이터를 가져오는 2초 동안 파이썬은 아무것도 안 하고 멍하니 기다립니다.

비동기(Asynchronous): 기다려야 하는 일이 생기면 "나중에 다 되면 알려줘!"라고 예약만 해두고, 그사이에 다른 일을 하러 갑니다.

비동기 코드 팁:
async def : 이함수는 비동기로 작동할 거다
await : 여기서 시간이 조금 걸리니까 결과가 나올 때까지 다른 일 하다와

비동기를 써야하는 이유
  만약, 10개의 API에서 데이터를 가져와야 한다고 가정할 때, 한 번에 1초식 걸린다면?
  동기방식 : 1초+1초+ .... +1초 = 총 10초 소요
  비동기방식: 10개를 동시에 요청하고 기다림 = 약 1초 소요

'''

import asyncio
import time

async def say_hello(name, delay):
  print(f"[{name}] 요청 시작 ...")
  await asyncio.sleep(delay) # 2. 기다리는 지점 지정(await)
  print(f"[{name}] {delay}초 만에 응답 완료!")


async def main():
  # time.strftime('%X'): 리눅스의 date +"%T"처럼 현재 시각을 17:05:30 같은 형식으로 예쁘게 보여줍니다.
  start_time = time.time()
  print(f"--- 전체 작업 시작 --- 시작시간 : {time.strftime('%X')}")
  
  #두 개의 작업을 동시에 던집니다!
  await asyncio.gather(
    say_hello("API-1",10),
    say_hello("API-2",5)
  )

  end_time = time.time()
  duration = end_time - start_time
  print(f"--- 전체 작업 종료 --- 종료시간 : {time.strftime('%X')}")
  print(f"총소요시간 {duration:.2f}초")

asyncio.run(main())

'''
출력
--- 전체 작업 시작 ---
[API-1] 요청 시작 ...
[API-2] 요청 시작 ...
[API-2] 1초 만에 응답 완료!
[API-1] 3초 만에 응답 완료!
--- 전체 작업 종료 ---
'''
