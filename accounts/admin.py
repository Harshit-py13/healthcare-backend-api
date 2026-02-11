from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'name', 'is_staff', 'is_active']
    ordering = ['email']

admin.site.register(User, CustomUserAdmin)