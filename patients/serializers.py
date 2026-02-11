from rest_framework import serializers
from .models import Patient # This looks for the class in models.py

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        read_only_fields = ["user", "created_at"]