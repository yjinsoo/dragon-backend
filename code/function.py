import time

# cpu_value가 80을 넘는지 확인하는 함수
def check_cpu(pod_name, cpu_value):
  if cpu_value >= 80:
    return f" {pod_name} 과부하!"
  else:
    return f" {pod_name} 정상!"

cluster_status = [
    {"name": "web-api", "status": "Running", "cpu_usage": 85, "memory": "256Mi"},
    {"name": "db-primary", "status": "Running", "cpu_usage": 30, "memory": "1Gi"},
    {"name": "cache-node", "status": "Error", "cpu_usage": 0, "memory": "0Mi"},
    {"name": "batch-worker", "status": "Pending", "cpu_usage": 0, "memory": "512Mi"},
    {"name": "auth-service", "status": "Running", "cpu_usage": 92, "memory": "128Mi"}
]


for pod in cluster_status:
  result=check_cpu(pod["name"],pod["cpu_usage"])
  print(result)

print("--- 모든 검사가 끝났습니다. Pod를 유지합니다. ---")
while True:
    time.sleep(60) # 60초마다 한 번씩 쉬면서 무한 대기
