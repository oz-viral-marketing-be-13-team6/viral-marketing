from django.db import models

class Users(models.Model):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', '관리자'
        USER = 'USER', '사용자'
        GUEST = 'GUEST', '손님'

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    # email 추가
    email = models.EmailField(max_length=256, unique=True)
    password = models.CharField(max_length=256)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
    )
    last_login = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    # view.py 용 이메일 검사
    is_active = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'
