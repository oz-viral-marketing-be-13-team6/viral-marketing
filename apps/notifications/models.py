from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    class Type(models.TextChoices):
        TRANSACTION = "transaction", "거래"
        LOW_BALANCE = "low_balance", "낮은 잔액"
        GOAL = "goal", "목표"
        SYSTEM = "system", "시스템"

    class Channel(models.TextChoices):
        IN_APP = "in-app", "앱 안에서"
        EMAIL = "email", "이메일"
        BOTH = "both", "둘 다"

    name = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50, blank=True, default="")
    role = models.CharField(max_length=20)

    type = models.CharField(max_length=20, choices=Type.choices)
    channel = models.CharField(max_length=20, choices=Channel.choices, default=Channel.IN_APP)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    condition_value = models.PositiveIntegerField(null=True, blank=True)
    condition_active = models.BooleanField(default=False)
    is_triggered = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "notifications"
        ordering = ["-created_at"]
