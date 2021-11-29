from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Communication

from eclinic_platform.serializers.communication_serializer import CommunicationSerializer

class CommunicationViewSet(viewsets.ModelViewSet):
    queryset            =   Communication.objects.all()
    serializer_class    =   CommunicationSerializer
    pagination_class    =   PageNumberPagination