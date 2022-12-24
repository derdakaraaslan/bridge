from typing import List
from ..models import EquipmentType
from . import api
from uuid import UUID
from .schemas import EquipmentTypeSchemaIn, EquipmentTypeSchemaOut, CreateResponseMessage, ResponseMessage, SearchSchema

'''
@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}
'''


@api.post("/equipment_type", tags=["Equipment Type"], response={200: CreateResponseMessage, 400: ResponseMessage, 403: ResponseMessage})
def create(request, payload: EquipmentTypeSchemaIn):
   
    try: 
        
        data = payload.dict()
        for eqipment in EquipmentType.objects.all():
            if eqipment.name == data["name"]:
                return 400, {"message": "Bu isimde bir kayıt mevcut."}
        object = EquipmentType()
        object.name = data["name"]
        object.save()
        return 200, {"message": "Ekipman başarıyla oluşturuldu.", "id": object.id}

    except Exception:
        return 403, {"message": "Bir hata oluştu."}


@api.get("/equipment_type/{uuid:equipment_type_id}", tags=["Equipment Type"], response={200: EquipmentTypeSchemaOut, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def read(request, equipment_type_id: UUID):
    try:
        object = EquipmentType.objects.get(pk=equipment_type_id)
    except EquipmentType.DoesNotExist:
        return 404, {"message": "Obje bulunamadı"}

    return 200, object


@api.put("/equipment_type/{uuid:equipment_type_id}", tags=["Equipment Type"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def update(request, payload: EquipmentTypeSchemaIn, equipment_type_id: UUID):
    object = EquipmentType.objects.get(id=equipment_type_id)

    data = payload.dict()
    for attr, value in data.items():
        setattr(object, attr, value)
    
    object.save()
    return 200, {"message": "Ekipman güncellendi"}


@api.delete("/equipment_type/{uuid:equipment_type_id}", tags=["Equipment Type"], response={200: ResponseMessage, 400: ResponseMessage, 403: ResponseMessage, 404: ResponseMessage})
def delete(request, equipment_type_id: UUID):
    object = EquipmentType.objects.get(id=equipment_type_id)
    object.is_active = False

    object.save()
    return 200, {"message": "Ekipman paylaşımı silindi"}


@api.post("/equipment_type/search", tags=["Equipment Type"], response={200: List[EquipmentTypeSchemaOut], 400: ResponseMessage})
def search(request, payload: SearchSchema):
    print(payload.search_on(EquipmentType, request.user))
    return payload.search_on(EquipmentType, request.user)
