cluster_status = [
    {"name": "web-api", "status": "Running", "cpu_usage": 85, "memory": "256Mi"},
    {"name": "db-primary", "status": "Running", "cpu_usage": 30, "memory": "1Gi"},
    {"name": "cache-node", "status": "Error", "cpu_usage": 0, "memory": "0Mi"},
    {"name": "batch-worker", "status": "Pending", "cpu_usage": 0, "memory": "512Mi"},
    {"name": "auth-service", "status": "Running", "cpu_usage": 92, "memory": "128Mi"}
]

#for문을 사용하여 전체 Pod검사
for pod in cluster_status:
  print(f"POD name:{pod['name']}, Pod Status:{pod['status']}, POD cpu_usage: {pod['cpu_usage']}, Pod memory_usage: {pod['memory']}
