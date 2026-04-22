pod_info = {
  "name" : "nginx-pod",
  "image" : "nginx:latest",
  "cpu": "500m",
  "memory": "128Mi"
}

for name,value in pod_info.itmes():
  print(f"key:{name}, value:{value}")
  
