'''
환경 변수 APP_ENV를 읽어옵니다. (기본값 "development")

만약 production이라면, logs_prod라는 폴더를 만드세요.

만약 development라면, logs_dev라는 폴더를 만드세요.

폴더를 만들기 전에 이미 존재하는지 확인하는 로직을 포함하세요. (os.path.exists)
'''

import time,os

app_env = os.environ.get("APP_ENV","development")
prd_file = "logs_prod"
dev_file = "logs_dev"

try:
  if app_env == "production" and not os.path.exists(prd_file): 
    os.makedirs(prd_file)
    current_dir = os.listdir(".")
    print(current_dir)
  elif app_env == "development" and not os.path.exists(dev_file):
    os.makedirs(dev_file)
    current_dir = os.listdir(".")
    print(current_dir)
  else:
    print("조건에 맞는 환경변수가 없습니다")
except Exception as e:
  print(f"Error check {e}")

print("==========END==========")
while True:
  time.sleep(60)
