from datetime import date
from ninja import ModelSchema
from ...models import CompanionRequest, AppUser


class CompanionRequestSchemaUser(ModelSchema):

    class Config:
        model = AppUser
        model_fields = ["id"]
        

class CompanionRequestSchemaOut(ModelSchema):
    owner: CompanionRequestSchemaUser
    class Config:
        model = CompanionRequest
        model_exclude = ["companion"]


class CompanionRequestSchemaIn(ModelSchema):
    owner: CompanionRequestSchemaUser
    class Config:
        model = CompanionRequest
        model_exclude = ["id", "is_active", "companion"]
