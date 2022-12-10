from datetime import date
from ninja import ModelSchema


class UserSchemaIn(ModelSchema):
    name: str
    surname: str
    password: str
