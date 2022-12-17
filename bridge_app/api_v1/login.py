from .schemas import AppUserSchemaLogin, AppUserSchemaOut, ResponseMessage
from ..models import AppUser
from . import api


@api.post("/login/app_user", tags=["Login"], response={200: AppUserSchemaOut, 400: ResponseMessage, 403: ResponseMessage}, auth=None)
def firm_user(request, payload: AppUserSchemaLogin):
    try:
        user = AppUser.objects.get(email=payload.email, is_active=True)
        if user.check_password(payload.password):
            return 200, user
        raise AppUser.DoesNotExist
    except AppUser.DoesNotExist:
        return 403, {"message": "Geçersiz kullanıcı adı ya da şifre."}
