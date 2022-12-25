from typing import List
from ..models import CompanionRequest, AppUser
from . import api
from uuid import UUID
from .schemas import CompanionRequestSchemaIn, CompanionRequestSchemaOut, CreateResponseMessage, ResponseMessage, SearchSchema

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/companion_request/create", tags=["Companion Request"], response={200: CreateResponseMessage, 400: ResponseMessage, 403: ResponseMessage})
def create(request, payload: CompanionRequestSchemaIn):
    
    try: 
        data = payload.dict()
        object = CompanionRequest()
        object.owner = AppUser.objects.get(pk=data["owner"]["id"])
        object.start_latitude = data["start_latitude"]
        object.start_longitude = data["start_longitude"]
        object.finish_latitude = data["finish_latitude"]
        object.finish_longitude = data["finish_longitude"]
        object.date = data["date"]
        object.title = data["title"]
        object.comment = data["comment"]
        object.save()
        return 200, {"message": "Refakatçi yardım talebi başarıyla oluşturuldu.", "id": object.id}

    except Exception as e:
        return 403, {"message": str(e)}


@api.get("/companion_request/{uuid:companion_request_id}", tags=["Companion Request"], response={200: CompanionRequestSchemaOut, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def read(request, companion_request_id: UUID):
    try:
        object = CompanionRequest.objects.get(pk=companion_request_id)
    except CompanionRequest.DoesNotExist:
        return 404, {"message": "Obje bulunamadı"}

    return 200, object


@api.put("/companion_request/{uuid:companion_request_id}", tags=["Companion Request"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def update(request, payload: CompanionRequestSchemaIn, companion_request_id: UUID):
    object = CompanionRequest.objects.get(id=companion_request_id)

    data = payload.dict()
    
    object.owner = AppUser.objects.get(pk=data["owner"]["id"])
    object.companion = AppUser.objects.get(pk=data["companion"]["id"])
    for attr, value in data.items():
        if(attr == "owner" or attr == "companion"):
            continue
        setattr(object, attr, value)
    
    object.save()
    return 200, {"message": "Refakatçi talebi güncellendi"}


@api.delete("/companion_request/{uuid:companion_request_id}", tags=["Companion Request"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def delete(request, companion_request_id: UUID):
    object = CompanionRequest.objects.get(id=companion_request_id)
    object.is_active = False

    object.save()
    return 200, {"message": "Refakatçi talebi silindi"}


@api.post("/companion_request/search", tags=["Companion Request"], response={200: List[CompanionRequestSchemaOut], 400: ResponseMessage})
def search(request, payload: SearchSchema):
    return payload.search_on(CompanionRequest, request.user)
