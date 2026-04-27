import time
from pydantic import BaseModel, Field

class User(BaseModel):
  id: int # 무조건 숫자여야 함
  username: str #무조건 문자열이어  truths



#테스트 데이터
data = { "id": "123", "username": "jinsoo" }

user = User(**data)

print(user.id)
print(type(user.id))

while True:
  time.sleep(60)
