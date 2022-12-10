from django.contrib import admin
from .models.user import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname']
