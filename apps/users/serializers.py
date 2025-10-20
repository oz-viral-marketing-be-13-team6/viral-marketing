from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Users
        fields = ["name", "email", "password", "nickname"]

    def create(self, validated_data):
        user = Users.objects.create(
            name=validated_data["name"],
            email=validated_data["email"],
            nickname=validated_data.get("nickname", ""),
            password=make_password(validated_data["password"]),  # 비밀번호 검사
            is_active=False  # 이메일 인증 후 활성화
        )
        return user
