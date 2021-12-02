from eclinic_platform.serializers.users_serializer import UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({ 'auth': True, 'refreshed': False })
        
        serialize_user = UserSerializer(self.user, many=False)
        _user = serialize_user.data
        _user["name"] = self.user.get_name()
        data.update({ 'user': _user })
        
        # and everything else you want to send in the response
        return data
    
class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer
    
   
