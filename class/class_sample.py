import time

class PodManager:
  #1. 초기화 메서드 : 객체를 만들 때 이름 등을 설정함
  def __init__(self, name, image) :
    self.name = name # self는 '이 기계 자신'을 뜻합니다.
    self.image = image
    self.status = "Stopped"

  def start(self):
    self.status = "Running"
    print(f" {self.name} 포드가 시작되었습니다! (이미지 : {self.image})")

#3. 사용하기(객체 생성)
my_pod = PodManager("web-api","nginx:latest")
my_pod.start() #매서드 호출

print("==========END==========")
while True:
  time.sleep(60)
