'''
os를 사용해 현재 경로에 app_data라는 폴더가 있는지 확인하고, 없으면 만드세요.
os.listdir()를 사용해 현재 경로의 모든 파일 목록을 가져옵니다.
반복문(for)을 사용해 파일 목록을 하나씩 확인하면서, 파일 이름에 .py가 포함된 파일이 몇 개인지 세어보세요. (힌트: if ".py" in file_name:)
최종적으로 **"발견된 파이썬 파일 개수: X개"**라고 출력하세요.
'''

import os, time

folder_name = "app_data"

if not os.path.exists(folder_name):
  os.makedirs(folder_name)
  print(f"{folder_name}폴더를 생성하였습니다.")
else:
  print(f"{folder_name}폴더가 이미 존재합니다.")

current_dir = os.listdir(".")
count = 0
for item in current_dir:
  try:
    if ".py" in itme:
      count += 1
  except Exception as e:
    print(f"Error check {e}")

print(f"발견된 파이썬 파일 개수: {count}개")


print("========end========")
while True:
  time.sleep(60)
