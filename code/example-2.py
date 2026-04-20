import time

students = [
    {"name": "Kim", "scores": [80, 90, 85]},
    {"name": "Lee", "scores": [100, 95, 90]},
    {"name": "Park", "scores": [60, 70, 65]},
    {"name": "Choi", "scores": [90, 90, 100]}
]


for stu in students:
    try:
        total=sum(stu["scores"])
        length=len(stu["scores"])
        print(f"{stu['name']} 의 평균점수는 {total/length}")
    except Exception as e:
        print(f"Error check {e}")

print("======== end ==========")
while true:
  time.sleep(30)
