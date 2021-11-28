from rest_framework import serializers, viewsets, status
from eclinic_platform.models import User

class UserSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = User
      #  fields = ['id', 'header_title', 'background_image', 'image', 'username', 'title', 'first_name', 'last_name', 'category', 'location_address', 'location_lat', 'location_lng', 'location_address_component', 'created_at', 'updated_at' ]
       fields = '__all__'




class SearchSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = User
      #  fields = ['id', 'header_title', 'background_image', 'image', 'username', 'title', 'category', 'location_address', 'location_lat', 'location_lng', 'location_address_component' ]
       fields = '__all__'

       name = serializers.SerializerMethodField()

       def get_name(self, instance):
          return instance.first_name+" "+instance.last_name

       def to_representation(self, instance):
           return {
              "username": instance.username,
              "name": self.get_name()
           }
           