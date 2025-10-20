# accounts/utils.py
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

def email_activator(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.user_id))
    token = default_token_generator.make_token(user)
    activation_link = f"http://{request.get_host()}/accounts/activate/{uid}/{token}/"

    send_mail(
        subject="계정 활성화 메일",
        message=f"아래 링크를 눌러 계정을 활성화 해주세요:\n{activation_link}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )
