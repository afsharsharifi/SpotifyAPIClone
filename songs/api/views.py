from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from extensions.permissions import UserGetAdminPostPutDeletePermission

from ..models import Genre, Like, Song
from .serializers import GenreSerializer, LikeSerializer, SongSerializer, SongUpdateSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "per_page"
    max_page_size = 1000


class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [UserGetAdminPostPutDeletePermission]
    pagination_class = StandardResultsSetPagination


class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [UserGetAdminPostPutDeletePermission]
    http_method_names = ["get", "put", "delete"]


class SongListCreateAPIView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [UserGetAdminPostPutDeletePermission]
    pagination_class = StandardResultsSetPagination


class SongRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    permission_classes = [UserGetAdminPostPutDeletePermission]
    http_method_names = ["get", "put", "delete"]

    def get_serializer_class(self):
        if self.request.method in ["GET", "DELETE"]:
            return SongSerializer
        elif self.request.method == "PUT":
            return SongUpdateSerializer


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
