from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Appointment
       fields = '__all__'