# Dockerfile

# 1. 베이스 이미지: Python 3.12 (pyproject.toml과 일치)
FROM python:3.12-slim-bookworm

# 2. 필수 패키지 설치:
# - build-essential: 일부 Python 패키지(예: psycopg2) 컴파일에 필요
# - netcat (netcat-openbsd): run.sh 스크립트에서 DB 연결 대기(nc)에 사용
RUN apt-get update && \
    apt-get install -y build-essential netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# 3. 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. 작업 디렉토리 설정
WORKDIR /app

# 5. Poetry 설치 및 설정
RUN pip install poetry
# Poetry에게 가상 환경을 만들지 않고 현재 컨테이너 환경에 설치하도록 지시
RUN poetry config virtualenvs.create false

# 6. 의존성 파일 복사 (Docker Layer Caching 활용)
COPY pyproject.toml poetry.lock /app/

# 7. 의존성 설치
# --no-root: 프로젝트 자체는 아직 패키징하지 않음
# --with dev,prod: 개발 및 배포 그룹의 의존성 모두 설치 (개발 환경용)
RUN poetry install --no-root --with dev,prod

# 8. 프로젝트 코드 복사
COPY . /app

# 9. 포트 노출
EXPOSE 8000

# 컨테이너 시작 시 실행될 명령어 (run.sh가 담당)
# CMD ["/app/scripts/run.sh"]