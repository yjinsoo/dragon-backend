from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta


# 암호화 알고리즘 설정 (bcrypt 사용)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "my_super_secret_key_dont_share_it"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 # 토큰 유효 시간 30분

# 1. 사용자가 입력한 평문 비밀번호를 암호화(Hash)하는 함수
def get_password_hash(password):
    return pwd_context.hash(password)

# 2. 입력받은 비번과 DB에 저장된 암호화된 비번이 일치하는지 확인하는 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire}) # 만료 시간 추가
    # 서버의 비밀키로 서명하여 토큰 생성
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user_name(token: str):
    try:
        print(f"DEBUG: 검증 시도하는 토큰 = {token[:20]}...")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM],options={"verify_exp": False})
        username: sstr = payload.get("Sub")
        print(f"DEBUG: 해독 성공! 유저명 = {username}")
        
        if username is None:
            return None
        return username
    except JWTError as e:
        print(f"DEBUG: JWT 해독 에러 발생! 사유 = {e}")
        return None
    
