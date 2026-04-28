from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional
import asyncio

user_list_db = {}
app=FastAPI()

class User(BaseModel):
  name: str
  age: int = Field(ge=0, le=100)

class UpdateUser(BaseModel):
  name: Optional[str] = None
  age: Optional[int] = Field(None, ge=0, le=100)
  

@app.post("/create-user")
async def create_user(user: User):
  if user.name in user_list_db:
    raise HTTPException(status_code=400, detail="이미 존재하는 USER")
  user_list_db[user.name] = user


@app.get("/check-user/{username}")
async def check_user(username: str):
  user = user_list_db.get(username)

  if not user:
    raise HTTPException(status_code=404, detail="해당 USER를 찾을 수없음")

  return user

@app.get("/list-user")
async def user_list():
  return user_list_db

@app.delete("/delete-user/{username}")
async def delete_user(username: str):
  user =  user_list_db.get(username)
  if not user:
    raise HTTPException(status_code=404, detail="해당 USER를 찾을 수 없음")
  # pod은 삭제하면서 그값을 리턴해 준다
  deleted_user=user_list_db.pop(username)
  
  return {"message": f"USER '{username}'가 성공적으로 삭제되었습니다.", "deleted_info": deleted_user}

@app.patch("/update-user/{username}")
async def update_user(username:str, updatedata: UpdateUser):
  update_user = user_list_db.get(username)
  if not update_user:
    raise HTTPException(status_code=404, detail="해당 USER를 찾을 수 없음")
    
  # 3. 보낸 데이터 중 '값이 있는 것'만 골라내기 (exclude_unset=True가 핵심!)
  # 클라이언트가 안 보낸 필드는 무시하고 실제 보낸 필드만 딕셔너리로 바꿉니다.
  update_dict = updatedata.model_dump(exclude_unset=True)


  for key, value in update_dict.items():
    setattr(current_user, key, value)

  return {
    "message": f"{username} user 업데이트 완료",
    "update data": update_user
  }






