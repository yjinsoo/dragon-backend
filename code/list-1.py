#리스트 만들기
pods = ["web-server", "db-server", "cache-server"]

#데이터 꺼내기
print(pods[0]) #결과 : web-server (첫번째 요소)
print(pods[-1])  # 결과 : cache-server (마지막 요소)

#데이터 추가하기
pods.append("api-server") # 맨 뒤에 추가됨


#딕셔너리 만들기 key, value형식
pod_info = {
  "name" : "nginx-pod",
  "image" : "nginx:latest",
  "cpu": "500m",
  "memory": "128Mi"
}

#데이터 꺼내기
print(pod_info["name"]) #결과 : nginx-pod
print(pod_inf["memory"]) 

#데이터 수정 및 추가
pod_info["memory"] = "256Mi"

#확인
print(pod_inf["memory"])
