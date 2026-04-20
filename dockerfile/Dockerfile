FROM python:3.9-slim

# 파이썬은 기본적으로 효율을 위해서 버퍼에 쌓아두고 한번에 출력하려하기때문에, 해당 옵션을 아예 끄기
# Pod log 즉각 출력을 하기 위함
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Flask 설치
# RUN pip install --no-cache-dir flask flask-cors

# 소스코드 복사
COPY code/try-except.py .

# Flask 포트
#EXPOSE 5000

# 실행
CMD ["python", "try-except.py"]
