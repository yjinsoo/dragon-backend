'''
asyncio 모듈을 import 하세요.

download_file(filename, duration)이라는 비동기 함수를 만드세요.

함수가 시작될 때 "{filename} 다운로드 시작..." 출력.

duration만큼 await asyncio.sleep() 하기.

완료되면 "{filename} 다운로드 완료! ({duration}초 소요)" 출력.

main() 함수에서 asyncio.gather()를 사용해 다음 세 파일을 동시에 다운로드하세요.

file_A: 5초 소요

file_B: 2초 소요

file_C: 3초 소요

총 소요 시간이 몇 초인지 확인해 보세요. (가장 긴 시간인 5초 만에 다 끝나야 성공입니다!)
'''

import time, asyncio

async def download_file(filename, duration):
  
