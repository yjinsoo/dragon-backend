from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import UserTable
from pydantic import BaseModel, Field
from typing import Literal, Optional
from auth import get_password_hash, verify_password, create_access_token


# 서버 기동 시 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic 모델 (여기 두셔도 되고 schemas.py로 빼도 됩니다)
class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=100)
    password: str # 사용자가 입력할 평문 비밀번호
    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=100)
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    name: str
    password: str # 사용자가 입력할 평문 비밀번호
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

@app.get("/user-list")
async def get_all_user(db: Session = Depends(get_db)):
    user = db.query(UserTable).all()
    return user

@app.post("/signup")
async def signup(user: User, db: Session = Depends(get_db)):
    # 1. 중복 체크 (기존과 동일)
    db_user = db.query(UserTable).filter(UserTable.name == user.name).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 존재하는 유저입니다.")
    
    # 2. 비밀번호 암호화 (인프라 보안의 핵심!)
    hashed_pwd = get_password_hash(user.password)
    
    # 3. DB 객체 생성 (암호화된 비번 저장)
    new_user = UserTable(
        name=user.name, 
        hashed_password=hashed_pwd, 
        age=user.age
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "회원가입 성공"}

@app.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    # 1. 유저 존재 확인
    db_user = db.query(UserTable).filter(UserTable.name == user.name).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="유저가 존재하지 않거나 비번이 틀림")
    
    # 2. 비밀번호 검증 (auth.py의 verify_password 사용)
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="유저가 존재하지 않거나 비번이 틀림")
    
    # 3. 검증 성공 시 토큰 발급
    access_token = create_access_token(data={"sub": db_user.name})
    
    return {"access_token": access_token, "token_type": "bearer"}


