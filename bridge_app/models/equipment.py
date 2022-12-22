from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.utils import IntegrityError

class EquipmentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    