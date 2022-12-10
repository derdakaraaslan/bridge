
from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.utils import IntegrityError


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def get_or_create(username, *args, **kwargs) -> "User":
        try:
            return User.objects.create_user(username, *args, **kwargs)
        except IntegrityError:
            return User.objects.get(username=username)

    class Meta:
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Tüm Kullanıcılar"
