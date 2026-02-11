from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer 
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)