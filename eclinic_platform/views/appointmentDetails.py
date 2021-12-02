from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import AppointmentDetails

from eclinic_platform.serializers.appointment_details_serializer import AppointmentDetailsSerializer

class AppointmentDetailsViewSet(viewsets.ModelViewSet):
    queryset            =   AppointmentDetails.objects.all()
    serializer_class    =   AppointmentDetailsSerializer
    pagination_class    =   PageNumberPagination