#!/bin/sh
set -e

# 1. DB 연결 대기 로직 추가
echo "Waiting for postgres..."
# nc(Netcat)을 사용하여 'db' 서비스의 5432 포트 연결을 계속 시도하며 대기합니다.
while ! nc -z db 5432; do
  sleep 0.2
done
echo "PostgreSQL started. Applying migrations..."

# 2. 마이그레이션 적용
python manage.py migrate --no-input

# 3. 개발 서버 실행 (자동 리로드 기능 활용)
exec python manage.py runserver 0.0.0.0:8000