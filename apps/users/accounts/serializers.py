# apps/accounts/serializers.py

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# ✅ JWT 커스텀 직렬화 (토큰에 사용자 정보 포함)
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 토큰에 추가로 담고 싶은 유저 정보
        token['username'] = user.username
        token['email'] = user.email

        return token

