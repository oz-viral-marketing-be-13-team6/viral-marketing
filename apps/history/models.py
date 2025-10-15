from django.db import models
from django.contrib.auth.models import User  # Django 기본 User 모델 참조


class TransactionHistory(models.Model):
    ROLE_CHOICES = [
        ('admin', '관리자'),
        ('user', '사용자'),
        ('guest', '손님'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")  # 사용자 ID (FK)
    transaction_id = models.AutoField(primary_key=True)  # 거래 고유 ID
    name = models.CharField(max_length=20, null=False)  # 이름
    password = models.CharField(max_length=128, null=False)  # 암호화된 비밀번호
    nickname = models.CharField(max_length=50, blank=True, null=True)  # 닉네임
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')  # 역할
    payment_method = models.CharField(max_length=30, blank=True, null=True)  # 결제 수단
    date = models.DateTimeField(auto_now_add=True)  # 거래 발생 시각
    category = models.CharField(max_length=50, blank=True, null=True)  # 거래 카테고리
    account_id = models.IntegerField(null=True, blank=True)  # 계좌 ID (FK 대체)

    def __str__(self):
        return f"[{self.transaction_id}] {self.name} ({self.role})"

    class Meta:
        db_table = "transaction_history"
        verbose_name = "사용자 거래내역"
        verbose_name_plural = "사용자 거래내역 목록"
