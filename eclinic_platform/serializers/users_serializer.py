from rest_framework import serializers, viewsets, status
from eclinic_platform.models import User

class UserSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = User
       fields = ['id', 'header_title', 'background_image', 'image', 'username', 'title', 'first_name', 'last_name', 'category', 'location_address', 'location_lat', 'location_lng', 'location_address_component', 'created_at', 'updated_at' ]
    #    fields = '__all__'