from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import Users
from .serializers import UserMeSerializer, UserPasswordChangeSerializer


# Create your views here.
# 게스트
DELETED_USERS_ID = 999999


class UserMeAPIView(APIView):
		permission_classes = [IsAuthenticated]

		def get(self, request):
				""" 로그인한 사용자 정보 조회 """
				ser = UserMeSerializer(request.user)
				return Response(ser.data)

		def put(self, request):
				"""" 수정 """
				ser = UserMeSerializer(request.user, data=request.data)
				ser.is_valid(raise_exception=True)
				ser.save()
				return Response(ser.data)

		def patch(self, request):
				""" 부분 수정 """
				ser = UserMeSerializer(request.user, data=request.data, partial=True)
				ser.is_valid(raise_exception=True)
				ser.save()
				return Response(ser.data)

		@transaction.atomic
		def delete(self, request):
				uesr: Users = request.user
				"""탈퇴하면 999999번 유저 활성화"""
				try:
						deleted_user = Users.objects.get(pk=DELETED_USERS_ID)
				except Users.DoesNotExist:
						return Response({'error': 'DELETED_USER(9999) 계정이 존재하지않습니다'}, status=400)

				from apps.accounts.models import Accounts
				Accounts.objects.filter(user=user).update(user=deleted_user)

				try:
						from apps.analysis.models import Analysis
						Analysis.objects.filter(user=user).update(user=deleted_user)
				except Exception:
						pass

				try:
						from apps.notifications.models import Notifications
						Notifications.objects.filter(user=user).update(user=deleted_user)
				except Exception:
						pass

				user.delete()


				return Response(status=status.HTTP_204_NO_CONTENT)


class UserPasswordChangeAPIView(APIView):
		permission_classes = [IsAuthenticated]

		def post(self, request):
				ser = UserPasswordChangeSerializer(data=request.data, context={'request': request})
				ser.is_valid(raise_exception=True)
				ser.save()
				return Response({'message': '비밀번호가 변경되었습니다'}, status=200)


