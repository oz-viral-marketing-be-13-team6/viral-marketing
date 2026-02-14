# config/settings/dev.py
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', '1234'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
				'OPTIONS': {
						'options': '-c client_encoding=UTF8',
				}
    }
}

# 1. 디버그 및 보안
DEBUG = True
ALLOWED_HOSTS = ['*'] # 개발 환경에서는 모든 호스트 허용

