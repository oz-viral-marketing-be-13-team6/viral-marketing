# apps/accounts/views.py

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CustomTokenObtainPairSerializer

# ✅ 로그인 (Access / Refresh Token 발급)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# ✅ Refresh Token으로 Access Token 재발급
class RefreshTokenView(TokenRefreshView):
    pass

