import time

#에러 만들기
#key값이 없는 경우 KeyError 발생
#error_data= [{ "name": "nginx-pod" }]

#for pod in error_data:
#  if pod["status"] == "Running":
#    print('정상입니다')

#Traceback (most recent call last):
#  File "/app/try-except.py", line 8, in <module>
#    if pod["status"] == "Running":
#KeyError: 'status'
cluster_status = [
    {"name": "web-api", "status": "Running", "cpu_usage": 85, "memory": "256Mi"},
    {"name": "db-primary", "status": "Running", "cpu_usage": 30, "memory": "1Gi"},
    {"name": "cache-node", "status": "Error", "cpu_usage": 0, "memory": "0Mi"},
    {"name": "batch-worker"},
    {"name": "auth-service", "status": "Running", "cpu_usage": 92, "memory": "128Mi"}
]

def check_cpu (pod):
  try:
    if pod["status"] == "Running" and pod["cpu_usage"] >= 80:
      return "Emergency"
    return "Normal"
  #key가 에러 처리
  except KeyError as e:
    return f"Data Error {e} key가 존재하지 않음"
  #그 외 모든 error 처리
  except Exception as e:
    return f"Error check {e}"
    
for pod in cluster_status:
  print(check_cpu(pod))

print("--- 모든 검사가 끝났습니다. Pod를 유지합니다. ---")
while True:
    time.sleep(60) # 60초마다 한 번씩 쉬면서 무한 대기
