from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PatientDoctorMapping

@admin.register(PatientDoctorMapping)
class MappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_at')
    list_filter = ('doctor', 'assigned_at')