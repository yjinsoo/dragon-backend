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
  #      score_avg=sum/len
        if total/length >= 90:
            print(f"장학금 대상자 {stu['name']}, 평균점수 {total/length}")
    except Exception as e:
        print(f"Error check {e}")



print("======== end ==========")
while True:
  time.sleep(60)
