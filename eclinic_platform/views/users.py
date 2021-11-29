from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import serializers, viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from eclinic_platform.models import User

from eclinic_platform.serializers.users_serializer import ProfileSerializer, SearchSerializer, UserSerializer
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