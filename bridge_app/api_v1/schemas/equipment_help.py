from datetime import date
from ninja import ModelSchema
from ...models import EquipmentHelp, AppUser
from . import AppUserSchemaOut, AppUserSchemaIn


class EquipmentHelpSchemaUser(ModelSchema):

    class Config:
        model = AppUser
        model_fields = ["id"]

class EquipmentHelpSchemaOut(ModelSchema):
    owner: EquipmentHelpSchemaUser
    
    class Config:
        model = EquipmentHelp
        model_fields = "__all__"


class EquipmentHelpSchemaIn(ModelSchema):
    owner: EquipmentHelpSchemaUser
    class Config:
        model = EquipmentHelp
        model_exclude = ["id", "is_active"]
