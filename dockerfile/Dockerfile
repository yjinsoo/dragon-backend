FROM python:3.9-slim

WORKDIR /app

# Flask 설치
# RUN pip install --no-cache-dir flask flask-cors

# 소스코드 복사
COPY code/loop-condition.py .

# Flask 포트
EXPOSE 5000

# 실행
CMD ["python", "loop-condition.py"]
