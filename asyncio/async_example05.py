'''
[조건]
check_db_connection()이라는 비동기 함수를 만듭니다.
이 함수는 실행될 때마다 await asyncio.sleep(0.5)를 합니다.
for 루프를 사용해 최대 3번 반복하며 접속을 시도하세요.
만약 접속에 실패하면(에러 가정), "재시도 중..."을 출력하고 다시 시도하세요.
마지막 3번째까지 실패하면 "최종 실패"를 출력하세요.

'''

import asyncio
import random

async def check_db_connection():
    for i in range(1, 4):
        print(f"📡 {i}번째 접속 시도 중...")
        await asyncio.sleep(0.5)
        
        # 50% 확률로 성공 또는 실패 시뮬레이션
        success = random.choice([True, False])
        
        if success:
            return "✅ DB 접속 성공!"  # 성공하면 즉시 종료!
        else:
            print("❌ 접속 실패...")
            
    return "🚨 3회 시도 모두 실패 (점검 필요)" # for문이 다 끝나면 실행

async def main():
    print("--- DB 점검 시작 ---")
    
    result = await check_db_connection()
    
    print(f"최종 결과: {result}")
    print("--- 점검 종료 ---")

if __name__ == "__main__":
    asyncio.run(main())
    
    
