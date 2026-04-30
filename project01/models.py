'''
DB를 객체처럼 다루게 해주는 + SQL 실행까지 해주는 라이브러리

models.py는 그 위에 올릴 '데이터베이스 스키마 설계도' 로생각하면 되며,
database.py에서 선언한 DB위에 하기 코드들로 table 생성 등을 진행
'''

from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from sqlalchemy.sql import func # 현재 시간을 가져오는 함수

class UserTable(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    age = Column(Integer)
    hashed_password = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
