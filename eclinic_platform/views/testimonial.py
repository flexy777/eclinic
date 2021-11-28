from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Testimonial

from eclinic_platform.serializers.testimonial_serializer import TestimonialSerializer

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset            =   Testimonial.objects.all()
    serializer_class    =   TestimonialSerializer
    pagination_class    =   PageNumberPagination