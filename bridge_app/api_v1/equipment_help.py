from typing import List
from ..models import EquipmentHelp, AppUser, EquipmentType
from . import api
from uuid import UUID
from .schemas import EquipmentHelpSchemaIn, EquipmentHelpSchemaOut, CreateResponseMessage, ResponseMessage, SearchSchema

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/equipment_help/create", tags=["Equipment Help"], response={200: CreateResponseMessage, 400: ResponseMessage, 403: ResponseMessage})
def create(request, payload: EquipmentHelpSchemaIn):
   
    try: 
        
        data = payload.dict()
        object = EquipmentHelp()
        object.title = data["title"]
        object.comment = data["comment"]
        object.equipment = EquipmentType.objects.get(pk=data["equipment"])
        object.owner = AppUser.objects.get(pk=data["owner"]["id"]) 
        object.save()
        return 200, {"message": "Ekipman paylaşımı başarıyla oluşturuldu.", "id": object.id}

    except Exception:
        return 403, {"message": "Bir hata oluştu."}


@api.get("/equipment_help/{uuid:equipment_help_id}", tags=["Equipment Help"], response={200: EquipmentHelpSchemaOut, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def read(request, equipment_help_id: UUID):
    try:
        object = EquipmentHelp.objects.get(pk=equipment_help_id)
    except EquipmentHelp.DoesNotExist:
        return 404, {"message": "Obje bulunamadı"}

    return 200, object


@api.put("/equipment_help/{uuid:equipment_help_id}", tags=["Equipment Help"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def update(request, payload: EquipmentHelpSchemaIn, equipment_help_id: UUID):
    object = EquipmentHelp.objects.get(id=equipment_help_id)

    data = payload.dict()
    
    object.owner = AppUser.objects.get(pk=data["owner"]["id"])
    object.equipment = EquipmentType.objects.get(pk=data["equipment"])
    for attr, value in data.items():
        if(attr == "owner" or attr == "equipment"):
            continue
        setattr(object, attr, value)
    
    object.save()
    return 200, {"message": "Ekipman paylaşımı güncellendi"}


@api.delete("/equipment_help/{uuid:equipment_help_id}", tags=["Equipment Help"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def delete(request, equipment_help_id: UUID):
    object = EquipmentHelp.objects.get(id=equipment_help_id)
    object.is_active = False

    object.save()
    return 200, {"message": "Ekipman paylaşımı silindi"}


@api.post("/equipment_help/search", tags=["Equipment Help"], response={200: List[EquipmentHelpSchemaOut], 400: ResponseMessage})
def search(request, payload: SearchSchema):
    return payload.search_on(EquipmentHelp, request.user)


@api.get("/equipment_help/photo/{uuid:equipment_help_id}", tags=["Equipment Help"], response={200: str, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def get_photo(request, equipment_help_id: UUID):
    try:
        object = EquipmentHelp.objects.get(pk=equipment_help_id)
        
    except EquipmentHelp.DoesNotExist:
        return 404, {"message": "Obje bulunamadı"}

    return 200, object.get_base64_equipment_photo