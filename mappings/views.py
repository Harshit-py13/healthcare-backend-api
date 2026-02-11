from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PatientDoctorMapping
from .serializers import MappingSerializer
from patients.models import Patient
from rest_framework.permissions import IsAuthenticated

permission_classes = [IsAuthenticated]


class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)

    def create(self, request, *args, **kwargs):
        patient_id = request.data.get("patient")
        try:
            Patient.objects.get(id=patient_id, user=request.user)
        except Patient.DoesNotExist:
            return Response(
                {"success": False, "message": "Patient not found or unauthorized"},
                status=status.HTTP_404_NOT_FOUND
            )
        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=["get"], url_path=r"patient/(?P<patient_id>\d+)")
    def get_patient_doctors(self, request, patient_id=None):
        try:
            patient = Patient.objects.get(id=patient_id, user=request.user)
        except Patient.DoesNotExist:
            return Response(
                {"success": False, "message": "Patient not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = MappingSerializer(mappings, many=True)
        return Response({"success": True, "data": serializer.data})