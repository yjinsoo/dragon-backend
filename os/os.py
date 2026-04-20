import os,time

#1. 환경변수 읽어오기
#os.environ.get(A,B)
# A환경변수값을 읽어와라, 없으면 B값을 사용
pod_host = os.environ.get("DB_HOST","localhost")
pod_lang = os.environ.get("LANG","kr")

#확인
print(f"pod_host: {pod_host}")
print(f"pod_lang: {pod_lang}")

#2. 현재 작업 디렉토리 확인
current_dir = os.getcwd()
print(f"현재 작업디렉토르 : {current_dir}")

print("==========end==========")
while True:
  time.sleep(60)
