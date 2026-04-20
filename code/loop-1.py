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
# 리스트안에 딕셔너리가 pod에 딕셔너리로 대입
##설명
# f-string의 구조
# f "문자열 {변수 or 계산식}"
# 문자열 앞에 알파벳 f를 붙이면 파이썬은 문자열 안에 있는 중괄호 {}를 여기는 코드가 들어갈 자리구나 인식
for pod in my_cluster:
  print(f"현대 검사중인 Pod: {pod['name']}")



#if문 결합
for pod in my_cluster:
  if pod["status"] == "Error":
    print(f"현재 pod상태이상 NAME: {pod['name']}, ID: {pod['id']}")
  else:
    print(f"정상 pod NAME: {pod['name]'}, ID: {pod['id']}")



