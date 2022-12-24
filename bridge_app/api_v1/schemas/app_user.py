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
        model_exclude = ["id", "user_permissions", "user_ptr", "username",
                         "groups", "is_active", "is_staff", "is_superuser", "date_joined", "last_login"
                         ]


class AppUserSchemaLogin(ModelSchema):

    class Config:
        model = AppUser
        model_exclude = ["id", "user_permissions", "user_ptr", "username", "first_name", "last_name",
                         "groups", "is_active", "is_staff", "is_superuser", "date_joined", "last_login", "is_disabled"]


class AppUserSchemaOutLogin(ModelSchema):

    class Config:
        model = AppUser
        model_exclude = ['password']


class AppUserSchemaForgotPassword(ModelSchema):

    class Config:
        model = AppUser
        model_exclude = ["id", "password", "user_permissions", "user_ptr", "username", "first_name", "last_name",
                         "groups", "is_active", "is_staff", "is_superuser", "date_joined", "last_login", "is_disabled"]


class AppUserSchemaChangeAvatar(ModelSchema):

    class Config:
        model = AppUser
        model_fields = ["id"]
