from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Favourite

from eclinic_platform.serializers.favourite_serializer import FavouriteSerializer

class FavouriteViewSet(viewsets.ModelViewSet):
    queryset            =   Favourite.objects.all()
    serializer_class    =   FavouriteSerializer
    pagination_class    =   PageNumberPagination