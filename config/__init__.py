import os
from .settings import dev

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')

if SETTINGS_MODULE == 'config.settings.prod':
    from .settings import prod as settings_module
elif SETTINGS_MODULE == 'config.settings.dev':
    from .settings import dev as settings_module
else:
    # 기본값: 개발 환경
    settings_module = dev

# 현재 모듈의 모든 속성을 settings_module에서 가져와 덮어씁니다.
for setting in dir(settings_module):
    if setting.isupper():
        globals()[setting] = getattr(settings_module, setting)