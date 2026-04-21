'''
requests 라이브러리
다른 서버(API)에 데이터를 달라고 요청하거나 응답하는데 사용
'''

import time,requests
from pprint import pprint

try:
  #1. 특정 주소에 GET 요청(데이터 달라고 하기)을 보냄
  response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

  print(dir(response))

  for check_item in response:
    print("리스트 내 내용확인")
    pprint(check_item)
  #2. 응답받은 데이터 파이썬 딕셔너리로 변경
  data = response.json()

  ## key를 모를 때 데이터 확인
  pprint(data)
  
  #3. 우리가 배운 딕셔너리 사용법으로 데이터 출력
  print(f"가져온 글제목: {data['title']}")

except Exception as e:
  print(f"데이터를 가져오는 중 에러 발생 {e}")

print("==========end==========")
while True:
  time.sleep(60)
