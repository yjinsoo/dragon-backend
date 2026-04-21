'''
환경 변수 APP_ENV를 읽어옵니다. (기본값 "development")

만약 production이라면, logs_prod라는 폴더를 만드세요.

만약 development라면, logs_dev라는 폴더를 만드세요.

폴더를 만들기 전에 이미 존재하는지 확인하는 로직을 포함하세요. (os.path.exists)
'''

import time,os

app_env = os.environ.get("APP_ENV","development")

if app_env == "production":
  os.

print("==========END==========")
while True:
  time.sleep(60)
