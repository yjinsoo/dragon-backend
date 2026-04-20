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
    for split in split_data:
      print(split)
  except Exception as e:
    print(f"error {e}")


while True:
  time.sleep(60)
