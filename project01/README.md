# 📦 database.py 코드 설명

---

## 1. Engine 생성

```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
```

- **Engine**: DB와 연결하는 핵심 객체 (드라이버 + 연결 통로 역할)
- SQLite 사용 시 필수 설정 포함

### ⚠️ SQLite 특징
- 기본적으로 **하나의 쓰레드만 DB 접근 가능**

### ✅ 해결
- `check_same_thread=False`
  - 여러 쓰레드에서 DB 접근 허용
  - FastAPI 같은 비동기 환경에서 필수 옵션

---

## 2. Session 생성

```python
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
```

- DB 작업을 위한 **세션 생성기**

### 옵션 설명

- `autocommit=False`
  - `db.commit()` 호출 전까지 DB 반영 ❌
  - → 트랜잭션 제어 가능

- `autoflush=False`
  - 자동 flush 비활성화
  - → 명시적 제어 가능

- `bind=engine`
  - 사용할 DB 엔진 지정

---

## 3. Base (모델 설계의 시작점)

```python
Base = declarative_base()
```

- ORM 모델의 **부모 클래스**

### 사용 예시

```python
class User(Base):
    __tablename__ = "users"
```

### 동작 원리
- Base를 상속한 클래스들을 SQLAlchemy가 추적
- → "이건 테이블이다" 인식
- → 이후 한 번에 테이블 생성 가능
- → "이제부터 이 Base를 상속받는 클래스들은 모두 DB 테이블로 관리하겠다"라고 선언한 것

---

## 4. get_db() (리소스 관리 핵심)

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### 동작 흐름

1. 요청 시 DB 세션 생성
2. `yield`로 API에 전달
3. 작업 종료 후 `db.close()` 실행

---

### 🔥 중요한 이유

- DB 커넥션은 **유한 자원**
- 반환 안 하면:
  - 커넥션 누수 발생
  - 커넥션 풀 고갈
  - 서비스 장애 발생 가능

---

### 🧠 인프라 관점 (Kubernetes)

- 커넥션 누수 발생 시:
  - 메모리 증가
  - DB 연결 한도 초과
  - Pod 장애 / 재시작

---

## ✅ 전체 요약

| 구성 요소 | 역할 |
|----------|------|
| Engine | DB 연결 통로 |
| SessionLocal | DB 작업 단위 |
| Base | ORM 모델의 부모 |
| get_db | 커넥션 관리 (핵심) |

---

# 📦 main.py 코드 설명

---

## 1. Class 생성

```python
class User(BaseModel):
    name: str
    age: int = Field(ge=0, le=100)
    class Config:
        from_attributes = True
```

- Class Config를 사용하는 이유
- 기본적으로 Pydantic은 데이터를 딕셔너리(dict) 형태로 읽는 것을 선호. 하지만 DB에서 데이터를 꺼내오면(SQLAlchemy), 데이터는 딕셔너리가 아니라 객체(Object) 형태

### 발생문제
- 딕셔너리 방식: user["name"] (Pydantic의 기본 기대치)
- 객체(속성) 방식: user.name (DB에서 꺼낸 데이터의 특징)

### ✅ 해결
- 옵션을 켜주면 Pydantic에게 이렇게 명령
- 데이터가 딕셔너리가 아니라 일반 객체(Attribute) 형태로 들어와도 당황하지 말고 알아서 잘 읽어줘

---
