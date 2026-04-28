Code 설명

database.py

1.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
엔진은 SQLite 파일에 접근하는 드라이버이자 연결통로
SQLite는 기본적으로 하나에 엔진에 하나의 쓰레드만 연결이가능하다.
FastAPI는 대부분 비동기식으로 여러 쓰레드가 한번에 DB에 접속을 해야하므로,
check_same_thread: False를 통해 이를 가능하게 해준다.

2.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
DB에 접속할수 있는 세션을 만들어 주는것
autocommit=False을 함으로써 db.commit()을 호출하기 전까지는 데이터를 영구 저장하지 않겠다는 뜻


3.
Base = declarative_base() (설계도 기초)
이것은 나중에 우리가 만들 models.py의 부모 클래스가 됩니다.

이 Base를 상속받아서 테이블을 만들면, SQLAlchemy가 "아, 이 클래스들은 내가 관리해야 할 DB 테이블들이구나!"라고 인식해서 나중에 한꺼번에 테이블을 생성해 줍니다.

 4.
get_db() (리소스 관리)
인프라에서 가장 중요한 '커넥션 풀 관리'와 관련이 있습니다.

yield db: API 요청이 들어오면 DB 연결을 하나 빌려줍니다.

finally: db.close(): 작업이 끝나면(성공하든 실패하든) 무조건 연결을 닫아서 메모리 누수를 방지합니다.

님이 Pod 안에서 리소스 모니터링을 할 때, 이 처리가 안 되어 있으면 DB 연결이 계속 쌓여서 서버가 뻗을 수도 있습니다.
