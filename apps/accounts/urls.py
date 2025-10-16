from django.urls import path
from .views import UserMeAPIView, UserPasswordChangeAPIView

urlpatterns = [
		path('me/', UserMeAPIView.as_view(), name='me'),
		path('me/password/', UserPasswordChangeAPIView.as_view(), name='user-me-password'),
]

#계정 관련없는 qpi