# config/settings/dev.py
from .base import *

# 1. 디버그 및 보안
DEBUG = True
ALLOWED_HOSTS = ['*'] # 개발 환경에서는 모든 호스트 허용

# ==============================
# ⚙️ Static Files (정적 파일 설정)
# ==============================
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",  # ✅ 여기가 bonobono.png가 들어있는 경로
]

STATIC_ROOT = BASE_DIR / "staticfiles"

