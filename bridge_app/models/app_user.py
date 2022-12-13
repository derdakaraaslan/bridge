
from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.utils import IntegrityError
from . import User


class AppUser(User):

    is_disabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Uygulama Kullanıcı"
        verbose_name_plural = "Tüm Uygulama Kullanıcılar"
