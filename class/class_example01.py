'''
ServiceChecker라는 클래스를 만듭니다.

__init__에서 서비스의 url을 입력받습니다.

check() 메서드를 만듭니다.

requests.get(url)을 사용해 접속을 시도합니다.

성공(200)하면 "✅ Service UP"을 반환합니다.

실패(에러 발생 시)하면 "❌ Service DOWN"을 반환합니다. (반드시 try-except 사용!)

테스트: https://jsonplaceholder.typicode.com/posts/1 주소를 사용하여 객체를 만들고 결과를 출력하세요.
'''

import time,requests

class ServiceChecker:
  def __init__(self,url):
    self.url = url

  def check(self):
    try:
      if requests.get(self.url):
        return "service up"
    except Exception as e:
      return "Service DOWN"

url_test = ServiceChecker("https://jsonplaceholder.typicode.com/posts/1")
print(url_test.check())

print("==========END==========")
while True:
  time.sleep(60)
  
