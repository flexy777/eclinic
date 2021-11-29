from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Review

class ReviewSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Review
       fields = '__all__'