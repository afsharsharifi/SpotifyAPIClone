from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from extensions.permissions import IsAdminOnlyPermission, UserGetAdminPostPutDeletePermission
from songs.api.serializers import SongSerializer
from songs.models import Song

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


class ArtistSongsListAPIView(APIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        artist = get_object_or_404(Artist, pk=pk)
        queryset = self.queryset.filter(artist=artist).annotate(q_count=Count("viewers_by_ip")).order_by("-q_count")
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
