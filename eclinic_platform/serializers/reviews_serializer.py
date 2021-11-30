from eclinic_platform.utilities.methods import toDateString, toFileUrl
from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Review

class ReviewSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Review
       fields = '__all__'
    
    date = serializers.SerializerMethodField()
    def get_date(self, instance):
        return toDateString(instance.created_at)
    
    reviewer = serializers.SerializerMethodField()
    
    def get_reviewer(self, instance):
        return {
            "name": instance.customer.first_name,
            "image": toFileUrl(instance.customer.image)
        }
    