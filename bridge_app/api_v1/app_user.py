from typing import List
from django.forms import ImageField
from ..models import AppUser
from . import api
from uuid import UUID
from .schemas import AppUserSchemaIn, AppUserSchemaOut, CreateResponseMessage, ResponseMessage, SearchSchema
from ninja.pagination import paginate

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/app_users", tags=["App User"], response={200: CreateResponseMessage, 400: ResponseMessage, 403: ResponseMessage})
def create(request, payload: AppUserSchemaIn):
    if AppUser.objects.filter(email=payload.dict()["email"]).exists():
        return 400, {"message": "Bu mail adresi zaten kayıtlı"}
    data = payload.dict()
    object = AppUser(**data)
    object.save()
    return 200, {"message": "Kullanıcı başarıyla oluşturuldu", "id": object.id}


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


@api.post("/app_users/search", tags=["Firm User"], response={200: List[AppUserSchemaOut], 400: ResponseMessage})
def search(request, payload: SearchSchema):
    return payload.search_on(AppUser, request.user)
