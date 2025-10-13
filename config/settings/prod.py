# config/settings/prod.py
from .base import *
import os
import environ

# 1. 환경 변수 로드
env = environ.Env()
# prod.py는 .env 파일에서 환경 변수를 읽어오지 않도록 설정 (배포 환경에 따라 달라짐)

# 2. 디버그 및 보안 (필수)
DEBUG = False
# 배포 환경에서는 반드시 ALLOWED_HOSTS를 실제 도메인으로 설정해야 합니다.
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['yourdomain.com'])

# 3. 데이터베이스 (PostgreSQL 연결)
# .env 파일에서 DB 연결 정보를 가져옵니다.
DATABASES = {'default': env.db()}

# 4. 정적 파일 (S3 또는 Gunicorn에서 처리)
STATIC_ROOT = BASE_DIR / 'staticfiles'