from rest_framework import generics

from extensions.permissions import IsAdminOnlyPermission, UserGetAdminPostPutDeletePermission

from ..models import Artist, User
from .serializers import ArtistSerializer, UserSerializer, UserUpdateSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOnlyPermission]


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAdminOnlyPermission]
    http_method_names = ["get", "put", "delete"]


# ? Artist Views


class ArtistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [UserGetAdminPostPutDeletePermission]


class ArtistRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [UserGetAdminPostPutDeletePermission]
    http_method_names = ["get", "put", "delete"]
