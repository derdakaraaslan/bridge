from datetime import date
from ninja import ModelSchema
from ...models import EquipmentType



class EquipmentTypeSchemaOut(ModelSchema):
    
    class Config:
        model = EquipmentType
        model_fields = "__all__"


class EquipmentTypeSchemaIn(ModelSchema):
    class Config:
        model = EquipmentType
        model_exclude = ["id", "is_active"]
