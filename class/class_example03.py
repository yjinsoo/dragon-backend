'''
Pod 클래스를 만듭니다. (name, cpu를 속성으로 가짐)

Pod 클래스 내부에 get_status() 메서드를 만듭니다.

CPU가 80 이상이면 "⚠️ Danger", 아니면 "OK"를 반환합니다.

반복문을 사용해 raw_data에 있는 딕셔너리들을 하나씩 Pod 객체로 만듭니다.

각 객체의 get_status() 결과와 이름을 예쁘게 출력하세요.
'''

import time

raw_data = [
    {"name": "web-01", "cpu": 45},
    {"name": "api-01", "cpu": 85},
    {"name": "db-01", "cpu": 92}
]

class Pod_status:
  def __init__(self,name,cpu):
    self.name =  name
    self.cpu = cpu

  def get_status(self):
    try:
      if self.cpu >= 80:
        return "Danger"
      else:
        return "OK"
    except Exception as e:


print("==========END==========")
while True:
  time.sleep(60)
  
