from rest_framework import generics, status
from rest_framework.response import Response

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone

from .models import Users
from .serializers import RegisterSerializer
from .utils import email_activator

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        email_activator(user, self.request)


class ActivateView(generics.GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = Users.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Users.DoesNotExist):
            return Response({"error": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)

        if default_token_generator.check_token(user, token):
            user.is_active = True

            user.email_verified_at = timezone.now()
            user.save()
            return Response({"message": "계정이 활성화되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "토큰이 유효하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
