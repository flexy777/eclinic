from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Transactions

from eclinic_platform.serializers.transactions_serializer import TransactionsSerializer

class TransactionsViewSet(viewsets.ModelViewSet):
    queryset            =   Transactions.objects.all()
    serializer_class    =   TransactionsSerializer
    pagination_class    =   PageNumberPagination