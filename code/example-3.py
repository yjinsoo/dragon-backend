import time

raw_logs = [
    "INFO:UserLoggedId:101",
    "ERROR:DatabaseConnectionFailed",
    "INFO:PaymentSuccess:202",
    "CRITICAL", # 데이터가 불완전함!
    "DEBUG:MemoryUsage:45%"
]

for log in raw_logs:
  try:
    split_data=log.split(":")
    if len(split_data) < 2:
        print(f"정상로그 아님 {log}")
        continue
    print(f"{split_data[0]},{split_data[1]},{split_data[2]}")
    
  except Exception as e:
    print(f"error {e}")


while True:
  time.sleep(60)
