from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Review

from eclinic_platform.serializers.reviews_serializer import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset            =   Review.objects.all()
    serializer_class    =   ReviewSerializer
    pagination_class    =   PageNumberPagination