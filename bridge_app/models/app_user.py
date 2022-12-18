
from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
import os
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import AbstractUser
from django.db.utils import IntegrityError
from . import User
import base64
from PIL import Image
import PIL
import numpy as np


class AppUser(User):

    is_disabled = models.BooleanField(default=False)
    profile_photo = models.ImageField(blank=True)
    
    def save(self, *args, **kwargs):
        super(AppUser, self).save(*args, **kwargs)
        if(self.profile_photo != ""):
            base_height = 480
            image = Image.open(f"./media/{self.profile_photo}")
            hpercent = (base_height / float(image.size[1]))
            wsize = int((float(image.size[0]) * float(hpercent)))
            image = image.resize((wsize, base_height), PIL.Image.ANTIALIAS)
            image.save(f'./media/{self.id}.jpg')
            os.remove(f"./media/{self.profile_photo}") 
        else:
            try:
                os.remove(f"./media/{self.id}.jpg") 
            except:
                pass
        

    @property
    def get_base64_profile_photo(self) -> str:
        try:
            with open(f"./media/{self.id}.jpg", 'rb') as img_file:
                b64_string = base64.b64encode(img_file.read())
            
            return b64_string
        except :
            return None
        
    
    class Meta:
        verbose_name = "Uygulama Kullanıcı"
        verbose_name_plural = "Tüm Uygulama Kullanıcılar"
