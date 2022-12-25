from django.db import models
import uuid
from .app_user import  AppUser

class CompanionRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey("AppUser", on_delete=models.PROTECT, related_name='creator')
    companion = models.ForeignKey("AppUser", on_delete=models.PROTECT, blank=True, null=True, related_name='companion')
    date = models.DateTimeField()
    start_latitude = models.CharField(max_length=20)
    start_longitude = models.CharField(max_length=20)
    finish_latitude = models.CharField(max_length=20)
    finish_longitude = models.CharField(max_length=20)
    comment = models.TextField()
    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=300, default="")

    
    
    
        
