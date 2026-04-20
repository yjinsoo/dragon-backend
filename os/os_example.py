'''
os 모듈을 import 하세요.
APP_ENV라는 이름의 환경 변수를 읽어옵니다. (기본값은 "development")
APP_PORT라는 이름의 환경 변수를 읽어옵니다. (기본값은 8080)
만약 APP_ENV가 "production"이면 **"🚨 운영 서버 가동 - 보안에 주의하세요"**를 출력하고, 그 외에는 **"🛠️ 개발 모드 실행 중"**을 출력하세요.
마지막에 **"서버 포트: {APP_PORT}"**를 f-string으로 출력하세요.
'''


import os,time

app_env = os.environ.get("APP_ENV","development")
app_port = os.environ.get("APP_PORT","8080")

try:
  if app_env == "production":
    print("운영서버 가동 - 보안에 주의하세요")
  else:
    print("개발 모드 실행 중")
except Exception as e:
  print(f"Error check {e}")

print(f"서버 포트: {app_port}")



print("===========end===========")
while True:
  time.sleep(60)
  
