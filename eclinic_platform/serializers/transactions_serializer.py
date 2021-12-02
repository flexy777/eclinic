from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Transactions

class TransactionsSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Transactions
       fields = '__all__'