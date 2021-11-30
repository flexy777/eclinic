from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Favourite
       fields = '__all__'