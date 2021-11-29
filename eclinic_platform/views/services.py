from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Services

from eclinic_platform.serializers.services_serializer import ServicesSerializer

class ServicesViewSet(viewsets.ModelViewSet):
    queryset            =   Services.objects.all()
    serializer_class    =   ServicesSerializer
    pagination_class    =   PageNumberPagination