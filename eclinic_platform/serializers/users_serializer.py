from rest_framework import serializers, viewsets, status
from eclinic_platform.models import User
from eclinic_platform.serializers.category_serializer import CategorySerializer

class UserSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = User
      #  fields = ['id', 'header_title', 'background_image', 'image', 'username', 'title', 'first_name', 'last_name', 'category', 'location_address', 'location_lat', 'location_lng', 'location_address_component', 'created_at', 'updated_at', 'avg_rating', 'checkup_Someone', 'online_Consult', 'home_Service' ]
       fields = '__all__'
      #  exclude = ('created_at', 'updated_at', 'password', 'is_staff')




class SearchSerializer(serializers.ModelSerializer):
           
      class Meta:
            model = User
            # fields = ['id', 'name', 'header_title', 'background_image', 'image', 'username', 'title', 'categories', 'location_address', 'location_lat', 'location_lng', 'location_address_component', 'avg_rating', 'checkup_Someone', 'online_Consult', 'home_Service' ]
            # fields = '__all__'
            exclude = ('created_at', 'updated_at', 'password', 'is_staff')

      name = serializers.SerializerMethodField()

      def get_name(self, instance):
         return instance.first_name+" "+instance.last_name

      # def to_representation(self, instance):
      #    return {
      #       "username": instance.username,
      #       "name": self.get_name()
      #    }
               
      categories = serializers.SerializerMethodField()
      
      def get_categories(self, instance):
         return CategorySerializer(instance.category, many=True).data