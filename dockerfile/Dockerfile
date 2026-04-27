FROM python:3.9-slim

# 파이썬은 기본적으로 효율을 위해서 버퍼에 쌓아두고 한번에 출력하려하기때문에, 해당 옵션을 아예 끄기
# Pod log 즉각 출력을 하기 위함
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Flask 설치
# RUN pip install --no-cache-dir flask flask-cors

#requests 설치
# 비동기 전용 라이브러리 httpx 추가 설치
#RUN pip install --no-cache-dir requests httpx

#fastapi 사용을 위한 라이브러리 설치
RUN pip install fastapi uvicorn httpx

#Pydantic 사용을 위한 라이브러리 설치
RUN pip install pydantic

# 소스코드 복사
COPY pydantic/pydantic_example01.py .

# Flask 포트
EXPOSE 8080

# 실행
CMD ["uvicorn", "pydantic_example01:app", "--host", "0.0.0.0", "--port", "8080"]
#CMD ["python", "pydantic_sample.py"]
