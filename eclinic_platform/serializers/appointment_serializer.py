from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Appointment, User
from eclinic_platform.serializers.transactions_serializer import TransactionsSerializer
from eclinic_platform.utilities.methods import shorten_user

class AppointmentSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Appointment
       fields = '__all__'

    patient = serializers.SerializerMethodField()

    def get_patient(self, instance):
        return shorten_user(instance.patient)


    specialist = serializers.SerializerMethodField()

    def get_specialist(self, instance):
        return shorten_user(instance.specialist)


    transaction = serializers.SerializerMethodField()

    def get_transaction(self, instance):
        return TransactionsSerializer(instance.transaction, many=False).data