from datetime import date
from ninja import ModelSchema
from ...models import User


class UserSchemaOut(ModelSchema):

    class Config:
        model = User
        model_exclude = ['password']


class UserSchemaIn(ModelSchema):

    class Config:
        model = User
        model_exclude = ["user_permissions", "id", "last_login", "date_joined"]
