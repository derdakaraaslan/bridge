
from django.forms import ImageField
from ..models import AppUser
from . import api
from uuid import uuid4
from .schemas import AppUserSchemaIn

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/appusers", tags=["AppUser"])
def create(request, payload: AppUserSchemaIn):
    print(payload.dict()["email"])
    print(AppUser.objects.filter(email=payload.dict()["email"]))
    if AppUser.objects.filter(email=payload.dict()["email"]).exists():
        return 400
    data = payload.dict()
    print(data)
    object = AppUser(**data)
    print(object)
    object.save()
    print("*********************")
    return 200
