from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
# 일반 유저 생성
  def create_user(self, email, password=None, **extra_fields):
    if not email:
        raise ValueError("이메일을 입력해주세요.")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)  # 비밀번호 해시
    user.save(using=self._db)
    return user

  # 슈퍼 유저 생성
  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)
    return self.create_user(email, password, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
  ROLE_CHOICES = [
    ('ADMIN', '관리자'),
    ('USER', '사용자'),
    ('GUEST', '손님'),
  ]

  user_id = models.AutoField(primary_key=True)
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=20)
  nickname = models.CharField(max_length=50, blank=True)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='USER')

  is_active = models.BooleanField(default=False)  # 이메일 인증 후 활성화
  is_staff = models.BooleanField(default=False)   # 관리자 여부
  created_at = models.DateTimeField(auto_now_add=True)
  email_verified_at = models.DateTimeField(blank=True, null=True)

  objects = UserManager()  # 위에서 만든 UserManager 연결

  USERNAME_FIELD = 'email'  # 로그인 시 사용할 필드
  REQUIRED_FIELD = ['name']  # 슈퍼유저 생성 시 필수 입력 필드

  def __str__(self):
    return self.email
