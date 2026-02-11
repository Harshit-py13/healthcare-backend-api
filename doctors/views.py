from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]