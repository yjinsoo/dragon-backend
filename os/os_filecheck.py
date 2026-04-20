'''
백엔드 서버나 Pod 환경에서는 로그 파일을 생성하거나, 특정 폴더 안에 파일이 있는지 확인해야 할 일이 정말 많습니다.
'''


import os,time

folder_name = "logs"

if not os.path.exists(folder_name):
  os.makedirs(folder_name)
  print(f"{folder_name}폴더를 생성하였습니다.")
else:
  print(f"{folder_name}폴더가 이미 존재합니다.")

current_dir = os.listdir(".")
print(f"현재 폴더 파일 목록: {current_dir}")

while True:
  time.sleep(60)
