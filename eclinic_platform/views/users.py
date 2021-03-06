from eclinic_platform.serializers.appointment_serializer import AppointmentSerializer
from eclinic_platform.serializers.reviews_serializer import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import Favourite, Review, User

from eclinic_platform.serializers.users_serializer import FavouriteSerializer, ProfileSerializer, SearchSerializer, UserSerializer
from eclinic_platform.utilities.methods import paginateQueryset

class UserViewSet(viewsets.ModelViewSet):
    queryset            =   User.objects.all()
    serializer_class    =   UserSerializer
    pagination_class    =   PageNumberPagination
    lookup_field        =   'username'



    @action(detail=False, methods=["post","get"], name="Search",  permission_classes=[])
    def search(self, request, pk=None):
        category = request.data.get("category", [])
        orderby = request.data.get("orderby", None)
        keyword = request.data.get("keyword", None)
        user = User.objects.all()
        return paginateQueryset(self, user, SearchSerializer)

    @action(detail=True, methods=["get"], name="Profile",  permission_classes=[])
    def profile(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            return Response(ProfileSerializer(user, many=False).data)
        except User.DoesNotExist:
            return Response({"detail" : "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=["get"], name="User Review",  permission_classes=[])
    def reviews(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            return paginateQueryset(self, Review.objects.filter(doctor=user), ReviewSerializer)
        except User.DoesNotExist:
            return Response({"detail" : "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)



    # Customers
    @action(detail=True, methods=["get"], name="Favourites",  permission_classes=[])
    def favourites(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            return paginateQueryset(self, user.get_favourites(), SearchSerializer)
        except User.DoesNotExist:
            return Response({"detail" : "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=False, methods=["post"], name="Search Username",  permission_classes=[])
    def checkuser(self, request, username=None):
        username = request.data.get("username", None)
        user = User.objects.filter(username=username).first()
        if(user):
            return Response({ "status": False, "detail": "Username already taken by another user." })
        return Response({ "status": True, "detail": "Username available" })



    @action(detail=True, methods=["get"], name="Appointment",  permission_classes=[])
    def appointments(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            return paginateQueryset(self, user.my_appointments(), AppointmentSerializer)
        except User.DoesNotExist:
            return Response({"detail" : "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)