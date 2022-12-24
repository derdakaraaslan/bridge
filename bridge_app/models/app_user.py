from django.db import models
from . import User
from django.core.validators import MaxValueValidator, MinValueValidator


class AppUser(User):
    is_disabled = models.BooleanField(default=False)
    avatar_id = models.PositiveIntegerField(
        default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def change_avatar_id(self):
        if (self.avatar_id == 5):
            self.avatar_id = 1
        else:
            self.avatar_id += 1

    class Meta:
        verbose_name = "Uygulama Kullanıcı"
        verbose_name_plural = "Tüm Uygulama Kullanıcılar"
