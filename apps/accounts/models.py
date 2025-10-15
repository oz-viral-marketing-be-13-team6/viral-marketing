from django.db import models
from .bank_code_choices import BankCode
from django_enum import EnumField

class Users(models.Model):
  class Role(models.TextChoices):
    ADMIN = 'ADMIN', '관리자'
    USER = 'USER', '사용자'
    GUEST = 'GUEST', '손님'

  user_id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  password = models.CharField(max_length=255)
  nickname = models.CharField(max_length=50, blank=True, null=True)
  role = EnumField(Role, default=Role.USER)
  last_login = models.DateTimeField()
  created_at = models.DateTimeField(blank=True, null=True)
  deleted_at = models.DateTimeField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'users'

class Accounts(models.Model):
    #계좌의 유형을 분리합니다
    class AccountTypes(models.TextChoices):
        CHECKING = "CHECKING", "입출금",
        SAVING = "SAVING", "적금",
        LOAN = "LOAN", "대출",
        PENSION = "PENSION", "연금",
        TRUST = "TRUST", "신탁",
        FOREIGN_CURRENCY = "FOREIGN_CURRENCY", "외화",
        IRP = "IRP", "퇴직연금",
        STOCK = "STOCK", "주식",
    account_type = models.CharField(
        max_length=25,
        choices=AccountTypes.choices,
        default=AccountTypes.CHECKING,
    )
    #은행의 코드
    bank_code = models.CharField(
        max_length=10,
        choices=BankCode.choices,
        default=BankCode.UNKNOWN,
        unique=True,
    )
    account_number = models.CharField(max_length=30, unique=True)
    balance = models.DecimalField(decimal_places=2, max_digits=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_bank_code_display()} ({self.account_number})"