from .schemas import AppUserSchemaLogin, AppUserSchemaOut, ResponseMessage, AppUserSchemaForgotPassword
from ..models import AppUser
from . import api
from django.core.mail import send_mail


@api.post("/login/app_user", tags=["Login"], response={200: AppUserSchemaOut, 400: ResponseMessage, 403: ResponseMessage}, auth=None)
def app_user(request, payload: AppUserSchemaLogin):
    try:
        user = AppUser.objects.get(email=payload.email, is_active=True)

        if user.check_password(payload.password):
            user.profile_photo = user.get_base64_profile_photo
            return 200, user
        raise AppUser.DoesNotExist
    except AppUser.DoesNotExist:
        return 403, {"message": "Geçersiz kullanıcı adı ya da şifre."}


@api.post("/login/app_user/forgot_password", tags=["Login"], response={200: bool, 400: ResponseMessage, 403: ResponseMessage}, auth=None)
def app_user(request, payload: AppUserSchemaForgotPassword):
    try:
        user = AppUser.objects.get(email=payload.email, is_active=True)
        password = AppUser.objects.make_random_password()
        user.set_password(password)
        user.save(update_fields=['password'])

        send_mail(
            'Bridge Şifre Sıfırlama İsteği',
            f'Yeni şifreniz: {password}',
            from_email='7derbia@gmail.com',
            recipient_list=[payload.email],
            fail_silently=False,
        )

        return 200, True
    except:
        return 403, {"message": "Bir hata oluştu"}
