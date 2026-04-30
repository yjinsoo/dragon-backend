from passlib.context import CryptContext

# 암호화 알고리즘 설정 (bcrypt 사용)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 1. 사용자가 입력한 평문 비밀번호를 암호화(Hash)하는 함수
def get_password_hash(password):
    return pwd_context.hash(password)

# 2. 입력받은 비번과 DB에 저장된 암호화된 비번이 일치하는지 확인하는 함수
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
