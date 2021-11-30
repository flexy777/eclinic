from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Communication, Favourite, Services, User
from eclinic_platform.serializers.category_serializer import CategorySerializer
from eclinic_platform.serializers.services_serializer import ServicesSerializer

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



class ProfileSerializer(serializers.ModelSerializer):

      class Meta:
            model = User
            # fields = ['id', 'name', 'header_title', 'background_image', 'image', 'username', 'title', 'categories', 'location_address', 'location_lat', 'location_lng', 'location_address_component', 'avg_rating', 'checkup_Someone', 'online_Consult', 'home_Service' ]
            # fields = '__all__'
            exclude = ('created_at', 'updated_at', 'password', 'is_staff')

      name = serializers.SerializerMethodField()

      def get_name(self, instance):
         return instance.first_name+" "+instance.last_name
      
      categories = serializers.SerializerMethodField()
      
      def get_categories(self, instance):
         return CategorySerializer(instance.category, many=True).data
         

      services = serializers.SerializerMethodField()
      
      def get_services(self, instance):
          services = Services.objects.filter(user=instance)
          return ServicesSerializer(services, many=True).data

      communications = serializers.SerializerMethodField()
      
      def get_communications(self, instance):
         modes = [
               {
                     "icon": "message-square",
                     "name": "In-App Chat"
               }
         ]
         comms = Communication.objects.filter(user=instance).first()
         if(not(comms is None)):
            if(comms.phone_enabled):
               modes.append({
                     "icon": "phone",
                     "name": "In-App Chat"
               })
               
            if(comms.email_enabled):
               modes.append({
                     "icon": "mail",
                     "name": "Email"
               })
               
            if(comms.whatsapp_enabled):
               modes.append({
                     "icon": "message-circle",
                     "name": "Whatapp"
               })
            if(comms.zoom_enabled):
               modes.append({
                     "icon": "video",
                     "name": "Zoom Meeting"
               })
            if(comms.google_meet_enabled):
               modes.append({
                     "icon": "plus",
                     "name": "Google Meet"
               })
            
         
         return modes


      extra_options = serializers.SerializerMethodField()
      
      def get_extra_options(self, instance):
        options = [
               {
                     "name": "online_consult",
                     "label": "Online Consult"
               }
         ]
         
        if(instance.checkup_someone):
               options.append({
               "name": "checkup_someone",
               "label": "Checkup Someone"
               })
                  
        if(instance.home_service):
               options.append({
                        "name": "home_service",
                        "label": "Home Service"
                  })
                  
        if(instance.free_consultation):
               options.append({
                        "name": "free_consultation",
                        "label": "Free Consultation"
                  })
        
        return options





class FavouriteSerializer(serializers.ModelSerializer):

      class Meta:
            model = User
            # fields = ['id', 'name', 'header_title', 'background_image', 'image', 'username', 'title', 'categories', 'location_address', 'location_lat', 'location_lng', 'location_address_component', 'avg_rating', 'checkup_Someone', 'online_Consult', 'home_Service' ]
            # fields = '__all__'
            exclude = ('created_at', 'updated_at', 'password', 'is_staff')


      
   


      def to_representation(self, instance):
          return {
                
          }