
from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.utils import IntegrityError
from . import User


class AppUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    password = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    is_active = models.BooleanField(default=True)
    is_disabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Uygulama Kullanıcı"
        verbose_name_plural = "Tüm Uygulama Kullanıcılar"
