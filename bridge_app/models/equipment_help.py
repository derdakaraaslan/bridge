from concurrent.futures import process
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from bridge_app.models.equipment import EquipmentType
from bridge_app.models.app_user import AppUser
import uuid
import PIL
from PIL import Image
import os
import base64

class EquipmentHelp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey("AppUser", on_delete=models.PROTECT)
    title = models.CharField(max_length=300)
    comment = models.TextField()
    equipment = models.ForeignKey(EquipmentType, on_delete=models.PROTECT)
    share_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    equipment_photo = models.ImageField(blank=True, upload_to='equipments')
    
    def save(self, *args, **kwargs):
        super(EquipmentHelp, self).save(*args, **kwargs)
        if(self.equipment_photo != ""):
            base_height = 480
            image = Image.open(f"./media/{self.equipment_photo}")
            hpercent = (base_height / float(image.size[1]))
            wsize = int((float(image.size[0]) * float(hpercent)))
            image = image.resize((wsize, base_height), PIL.Image.ANTIALIAS)
            image.save(f'./media/equipments/{self.id}.jpg')
            os.remove(f"./media/{self.equipment_photo}") 
        else:
            try:
                os.remove(f"./media/{self.id}.jpg") 
            except:
                pass
        

    @property
    def get_base64_equipment_photo(self) -> str:
        try:
            print(self.id)
            with open(f"./media/equipments/{self.id}.jpg", 'rb') as img_file:
                b64_string = base64.b64encode(img_file.read())
            
            return b64_string
        except :
            return None