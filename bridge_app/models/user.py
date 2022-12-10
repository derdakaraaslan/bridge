
from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
import uuid
import datetime
# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField(default="User")
    surname = models.TextField(default="Karaaslan")
    age = models.IntegerField(default=0)
    password = models.TextField()
