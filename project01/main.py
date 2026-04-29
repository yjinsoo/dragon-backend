from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import UserTable
from pydantic import BaseModel, Field
from typing import Literal, Optional


# 서버 기동 시 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic 모델 (여기 두셔도 되고 schemas.py로 빼도 됩니다)
class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=100)
    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=100)
    class Config:
        from_attributes = True


#USER 생성
@app.post("/create-user")
async def create_user(user: User, db: Session = Depends(get_db)):
    db_user = db.query(UserTable).filter(UserTable.name == user.name).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 USER")
    
    new_user = UserTable(name=user.name, age=user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#USER 조회
@app.get("/get-user/{username}")
async def get_user(username: str, db: Session = Depends(get_db)):
    get_user = db.query(UserTable).filter(UserTable.name == username).first()
    # get_user에 조건에 일치하는 user의 메모리 주소가 대입되면 True
    # get_user에 조건에 일치하지않아 None값이 담기면 False
    if not get_user:
        raise HTTPException(status_code=404, detail="존재하지 않는 USER")
    return get_user

#USER 삭제
@app.delete("/delete-user/{username}")
async def delete_user(username: str, db: Session = Depends(get_db)):
    delete_user = db.query(UserTable).filter(UserTable.name == username).first()
    if not delete_user:
        raise HTTPException(status_code=404, detail="삭제할 USER가 존재하지 않음")
    db.delete(delete_user)
    db.commit()
    return { "message" : f"{username} 삭제완료" }

#USER 업데이트
@app.patch("/update-user/{username}")
async def update_user(username: str, updatedata: UpdateUser, db: Session = Depends(get_db)):
    update_user = db.query(UserTable).filter(UserTable.name == username).first()
    if not update_user:
        raise HTTPException(status_code = 404, detail="Update할 USER가 존재하지 않음")
    update_dic = updatedata.model_dump(exclude_unset = True)
    for key, value in update_dic.items():
        setattr(update_user,key,value)

    db.commit()
    db.refresh(update_user)
    
    return update_user

@app.post("/users")
async def create_user(user: User, db: Session = Depends(get_db)):
    new_user = UserTable(name=user.name, age=user.age)
    db.add(new_user)
    db.commit() # 여기서 이미 디스크에는 저장됨!

    # [중요] refresh 전의 상태 확인
    print(f"--- Refresh 전 ---")
    print(f"ID: {new_user.id}")         # None 혹은 에러가 날 수 있음
    print(f"생성시각: {new_user.created_at}") # None
    
    db.refresh(new_user) # 이제 DB와 동기화!

    # [중요] refresh 후의 상태 확인
    print(f"--- Refresh 후 ---")
    print(f"ID: {new_user.id}")         # DB가 부여한 실제 ID (예: 1)
    print(f"생성시각: {new_user.created_at}") # DB가 기록한 실제 시간 (예: 2026-04-29...)
    
    return new_user


    



