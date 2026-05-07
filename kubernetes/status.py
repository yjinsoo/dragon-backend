from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.responses import StreamingResponse
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


def get_headers(token_path):
        with open(token_path, "r") as f:
                TOKEN = f.read().strip()
        headers = {
                "Authorization": f"Bearer {TOKEN}",
                "Accept": "application/json"
        }
        return headers
  

@app.get("/pods/{namespace}")
async def get_pods(namespace: str):
        url = f"https://{host}:{port}/api/v1/namespaces/{namespace}/pods"
        headers = get_headers(token_path)
        async with httpx.AsyncClient(verify=ca_cert_path) as client:
                response = await client.get(url, headers=headers, timeout=10.0)
        return response.json()
        
@app.get("/pods/{namespace}/{podname}")
async def get_pods_status(namespace: str, podname: str):
        url = f"https://{host}:{port}/api/v1/namespaces/{namespace}/pods/{podname}"
        headers = get_headers(token_path)
        async with httpx.AsyncClient(verify=ca_cert_path) as client:
                response = await client.get(url, headers=headers, timeout=10.0)
        return response.json()["status"]["phase"]


@app.get("/pods/{namespace}/{podname}/logs")
async def get_pod_logs(namespace: str, podname: str):
        url = f"https://{host}:{port}/api/v1/namespaces/{namespace}/pods/{podname}/log"
        headers = get_headers(token_path)
        client = httpx.AsyncClient(verify=ca_cert_path)

        async def request_stream():
                async with client.stream("GET",url, headers=headers) as r:
                        async for chunk in r.aiter_raw():
                                yield chunk
        return StreamingResponse(request_stream())


if __name__ == "__main__":
    asyncio.run(main())
