'''
Pod라는 이름의 클래스를 만드세요.
__init__ 메서드에서 name, cpu_usage를 입력받아 저장하세요.
is_overload라는 메서드를 만드세요.

이 메서드는 self.cpu_usage가 80 이상이면 True, 아니면 False를 돌려줍니다(return).

객체 생성 및 테스트:
이름이 "DB-Pod", CPU가 90인 객체를 하나 만드세요.
만약 이 객체의 is_overload()가 True라면 "⚠️ 경고: {이름} 과부하!"를 출력하세요.
'''
import time

class Pod:
  def __init__(self, name, cpu_usage):
    self.name = name
    self.cpu_usage = cpu_usage
    
  def is_overload(self):
    if self.cpu_usage >= 80 :
      return True
    else:
      return False
  
object01 = Pod("DB-Pod",90)
print(object01.is_overload())


print("==========END==========")
while True:
  time.sleep(60)
