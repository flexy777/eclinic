from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Categories

from eclinic_platform.serializers.category_serializer import CategorySerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset            =   Categories.objects.all()
    serializer_class    =   CategorySerializer
    pagination_class    =   None

