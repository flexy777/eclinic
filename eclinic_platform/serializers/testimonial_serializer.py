from rest_framework import serializers, viewsets, status
from eclinic_platform.models import Testimonial

class TestimonialSerializer(serializers.ModelSerializer):
           
    class Meta:
       model = Testimonial
       fields = '__all__'