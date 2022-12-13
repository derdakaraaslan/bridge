from django.contrib import admin
from .models import User, AppUser

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['id', "first_name", "username", "email", "password"]
