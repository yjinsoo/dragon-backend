import time
from pydantic import BaseModel, Field

class User(BaseModel):
  id: int # 무조건 숫자여야 함
  username: str #무조건 문자열이어  truths

class ServerConfig(BaseModel):
  name: str
  #port는 최소 1024, 최대 65535이어야 함
  port: int = Field(ge=1024, le=65535)
  #vcpu는 1,2,4,8중 하나여야 함
  vcpu: int = Field(description="CPU 코어 수")

#테스트 데이터
data = { "id": "123", "username": "jinsoo" }

user = User(**data)

print(user.id)
print(type(user.id))


print(ServerConfig(name="web-server", port=8080, vcpu=2))

try:
  ServerConfig(name="db-server", port=80, vcpu=2)
except Exception as e:
  print(f"error check {e}")


while True:
  time.sleep(60)
