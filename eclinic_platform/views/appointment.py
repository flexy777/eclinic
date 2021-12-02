from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Appointment

from eclinic_platform.serializers.appointment_serializer import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset            =   Appointment.objects.all()
    serializer_class    =   AppointmentSerializer
    pagination_class    =   PageNumberPagination