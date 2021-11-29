from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Services

class ServicesSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Services
       fields = '__all__'