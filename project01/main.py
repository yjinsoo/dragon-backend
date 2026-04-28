from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import engine, get_db, Base
from .models import UserTable
from pydantic import BaseModel, Field

# 서버 기동 시 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic 모델 (여기 두셔도 되고 schemas.py로 빼도 됩니다)
class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=100)
    class Config:
        from_attributes = True

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
