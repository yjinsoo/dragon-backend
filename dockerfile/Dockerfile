FROM python:3.9-slim

WORKDIR /app

# 필요한 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY app.py .

# Flask 포트 개방
EXPOSE 5000

# 실행
CMD ["python", "app.py"]
