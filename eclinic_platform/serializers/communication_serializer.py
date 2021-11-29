from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Communication

class CommunicationSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Communication
       fields = '__all__'