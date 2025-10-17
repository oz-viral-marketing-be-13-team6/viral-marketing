from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# ✅ JWT 발급 시 커스터마이징용 Serializer
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # 🔹 원하는 사용자 정보 토큰에 추가
        token['username'] = user.username
        token['email'] = user.email

        return token
