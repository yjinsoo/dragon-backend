from fastapi import FastAPI, HTTPException, Depends, Header
from sqlalchemy.orm import Session
import httpx  # 비동기 전용 requests 같은 놈
from pydantic import BaseModel, Field
from typing import Literal, Optional
import os


app = FastAPI()

# 1. 환경 변수에서 API 서버 주소 가져오기
host = os.environ.get("KUBERNETES_SERVICE_HOST")
port = os.environ.get("KUBERNETES_SERVICE_PORT")
APISERVER = f"https://{host}:{port}"
ca_cert_path = "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt"
token_path = "/var/run/secrets/kubernetes.io/serviceaccount/token"

def get_token(
with open(token_path, "r") as f:
    TOKEN = f.read().strip()

# 3. HTTP 헤더 구성
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json"
}

@app.get("/pods")
async def get_pods():
    url = f"https://{host}:{port}/api/v1/namespaces/default/pods"
    print(f"{url},{TOKEN}")
    async with httpx.AsyncClient(verify=ca_cert_path) as client:
        response = await client.get(url, headers=headers, timeout=10.0)
    return response.json

if __name__ == "__main__":
    asyncio.run(main())
