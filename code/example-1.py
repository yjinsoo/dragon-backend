import time

inventory = [
    {"item": "Milk", "price": 2500, "count": 10},
    {"item": "Bread", "price": 1500, "count": 0},
    {"item": "Coffee", "price": 3000, "count": 5},
    {"item": "Snack", "price": 2000, "count": 2}
]

def check_inventory(item_list):
  try:
      if item_list["count"] == 0:
          return "품절"
      elif item_list["count"] <= 3:
          return" 재입고 필요"
      else:
          return "판매 중"
  except Exception as e:
    return f"error 확인 필요 {e}"

for inven in inventory:
    print(check_inventory(inven))
    

print("--- 모든 검사가 끝났습니다. Pod를 유지합니다. ---")
while True:
    time.sleep(60) # 60초마다 한 번씩 쉬면서 무한 대기
