# config/settings/dev.py
from .base import *

# 1. 디버그 및 보안
DEBUG = True
ALLOWED_HOSTS = ['*'] # 개발 환경에서는 모든 호스트 허용

# 2. 데이터베이스
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}