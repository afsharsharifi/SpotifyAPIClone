from django.db.models import Count
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from extensions.permissions import AloowAllGetAdminPostPutDeletePermission
from users.models import UserIP

from ..models import Genre, Like, Song
from .serializers import GenreSerializer, LikeSerializer, SongSerializer, SongUpdateSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "per_page"
    max_page_size = 1000


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AloowAllGetAdminPostPutDeletePermission]
    pagination_class = StandardResultsSetPagination


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AloowAllGetAdminPostPutDeletePermission]
    http_method_names = ["get", "put", "delete"]


class SongListCreateAPIView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [AloowAllGetAdminPostPutDeletePermission]
    pagination_class = StandardResultsSetPagination


class SongRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    permission_classes = [AloowAllGetAdminPostPutDeletePermission]
    http_method_names = ["get", "put", "delete"]

    def get_serializer_class(self):
        if self.request.method in ["GET", "DELETE"]:
            return SongSerializer
        elif self.request.method == "PUT":
            return SongUpdateSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, args, kwargs)
        song = get_object_or_404(Song, pk=response.data["id"])
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        ip = ""
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        ip_obj, created = UserIP.objects.get_or_create(user_ip=ip)
        song.viewers_by_ip.add(ip_obj)
        return response


class PopularSongsAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = self.queryset.annotate(q_count=Count("likes")).order_by("-q_count")
        return queryset


class LikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LikeSerializer,
        responses=LikeSerializer,
    )
    def post(self, request, format=None):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            like_obj = Like.objects.filter(user=self.request.user, song=request.data.get("song"))
            if like_obj.exists():
                return Response({"detail": "شما قبلا این آهنگ را لایک کرده اید"}, status=status.HTTP_409_CONFLICT)
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(request=LikeSerializer, responses=LikeSerializer)
    def post(self, request, format=None):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            like_obj = Like.objects.filter(user=self.request.user, song=request.data.get("song"))
            if not like_obj.exists():
                return Response({"detail": "این آهنگ توسط شما لایک نشده است"}, status=status.HTTP_409_CONFLICT)
            Like.objects.filter(user=self.request.user, song=request.data.get("song")).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteSongsAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user_likes = Like.objects.filter(user=self.request.user)
        liked_songs = [like.song for like in user_likes]
        return liked_songs
