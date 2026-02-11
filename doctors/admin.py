from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience', 'hospital')
    search_fields = ('name', 'specialization')