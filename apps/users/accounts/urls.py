# apps/accounts/urls.py

from django.urls import path
from .views import LoginView
from .views import UserMeAPIView, UserPasswordChangeAPIView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
		path('me/', UserMeAPIView.as_view(), name='me'),
		path('me/password/', UserPasswordChangeAPIView.as_view(), name='user-me-password'),
]

#계정 관련없는 qpi