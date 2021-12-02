from rest_framework import serializers, viewsets, status
from eclinic_platform.models import AppointmentDetails

class AppointmentDetailsSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = AppointmentDetails
       fields = '__all__'