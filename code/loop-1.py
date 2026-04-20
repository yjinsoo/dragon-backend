##반복문
#리스트 for문으로 출력하기
pods = ["web-server", "db-server", "cache-server"]

#딕셔너리 만들기 key, value형식
pod_info = {
  "name" : "nginx-pod",
  "image" : "nginx:latest",
  "cpu": "500m",
  "memory": "128Mi"
}

# 리스트 안에 딕셔너리
my_cluster=[
  {"id":1, "name": "auth-pod", "status": "Running"},
  {"id":2, "name": "payment-pod", "status": "Pending"},
  {"id":3, "name": "search-pod", "status": "Error"}
]


#출력
for pod in my_cluster:
  print(f"현대 검사중인 Pod: {pod['name']}")
