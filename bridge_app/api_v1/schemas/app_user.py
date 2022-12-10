from datetime import date
from ninja import ModelSchema
from ...models import AppUser


class AppUserSchemaOut(ModelSchema):

    class Config:
        model = AppUser
        model_exclude = ['password']


class AppUserSchemaIn(ModelSchema):

    class Config:
        model = AppUser
        model_exclude = ["id", "is_active"]
