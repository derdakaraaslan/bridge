from typing import List
from ..models import AppUser
from . import api
from uuid import UUID
from .schemas import AppUserSchemaIn, AppUserSchemaOut, CreateResponseMessage, ResponseMessage, SearchSchema, AppUserSchemaChangeAvatar

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/app_users", tags=["App User"], response={200: CreateResponseMessage, 400: ResponseMessage, 403: ResponseMessage})
def create(request, payload: AppUserSchemaIn):

    try:
        if AppUser.objects.filter(email=payload.dict()["email"]).exists():
            return 400, {"message": "Bu mail adresi zaten kayıtlı."}

        data = payload.dict()

        username = AppUser.objects.filter(
            first_name=data["first_name"], last_name=data["last_name"])
        object = AppUser(**data)

        object.username = data["first_name"] + \
            data["last_name"]+str(len(username)+1)

        object.set_password(payload.password)
        object.save()

        return 200, {"message": "Kullanıcı başarıyla oluşturuldu.", "id": object.id}

    except Exception as e:
        return 403, {"message": str(e)}


@api.get("/app_users/{uuid:app_user_id}", tags=["App User"], response={200: AppUserSchemaOut, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def read(request, app_user_id: UUID):
    try:
        object = AppUser.objects.get(pk=app_user_id)
    except AppUser.DoesNotExist:
        return 404, {"message": "Kullanıcı bulunamadı"}

    return 200, object


@api.put("/app_users/{uuid:app_user_id}", tags=["App User"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def update(request, payload: AppUserSchemaIn, app_user_id: UUID):
    object = AppUser.objects.get(id=app_user_id)

    data = payload.dict()

    for attr, value in data.items():
        setattr(object, attr, value)

    object.save()
    return 200, {"message": "Kullanıcı güncellendi"}


@api.delete("/app_users/{uuid:app_user_id}", tags=["App User"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def delete(request, app_user_id: UUID):
    object = AppUser.objects.get(id=app_user_id)
    object.is_active = False

    object.save()
    return 200, {"message": "Kullanıcı silindi"}


@api.post("/app_users/search", tags=["App User"], response={200: List[AppUserSchemaOut], 400: ResponseMessage})
def search(request, payload: SearchSchema):
    return payload.search_on(AppUser, request.user)


@api.post("/app_users/change_avatar", tags=["App User"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage})
def change_avatar(request, payload: AppUserSchemaChangeAvatar):

    try:
        user = AppUser.objects.get(pk=payload.id)
        user.change_avatar_id()
        user.save()

        return 200, {"message": user.avatar_id}

    except Exception as e:
        return 403, {"message": str(e)}
