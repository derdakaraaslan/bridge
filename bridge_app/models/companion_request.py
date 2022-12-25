from django.db import models
import uuid

class CompanionRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey("AppUser", on_delete=models.PROTECT, related_name='creator')
    companion = models.ForeignKey("AppUser", on_delete=models.PROTECT, blank=True, null=True, related_name='companion')
    date = models.DateTimeField()
    start_latitude = models.CharField(max_length=10)
    start_longitude = models.CharField(max_length=10)
    finish_latitude = models.CharField(max_length=10)
    finish_longitude = models.CharField(max_length=10)
    comment = models.TextField()
    is_active = models.BooleanField(default=True)
    
        
