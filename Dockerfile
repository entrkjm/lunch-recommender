FROM python:3.12-slim

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# Cloud Run은 기본적으로 8080 포트를 사용합니다.
EXPOSE 8080

# 애플리케이션 실행 (app.py가 엔트리포인트)
CMD ["python", "app.py"]
