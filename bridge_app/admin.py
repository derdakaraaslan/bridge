from django.contrib import admin
from .models import User, AppUser, EquipmentType, EquipmentHelp, CompanionRequest

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['id', "first_name", "username", "email", "password"]
    
@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ['id', "name"]
    
@admin.register(EquipmentHelp)
class EquipmentHelpAdmin(admin.ModelAdmin):
    list_display = ['id', "owner", "title", "share_date"]
    
@admin.register(CompanionRequest)
class CompanionRequestAdmin(admin.ModelAdmin):
    list_display = ['id', "owner","companion",  "date", "title"]
