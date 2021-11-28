from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Categories

class CategorySerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Categories
       exclude = ('created_at', 'updated_at')
    #    fields = '__all__'