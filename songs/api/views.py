from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from extensions.permissions import IsAdminOnlyPermission

from ..models import Genre, Like, Song
from .serializers import (
    GenreSerializer,
    LikeSerializer,
    SongCreateSerializer,
    SongRetrieveSerializer,
)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "per_page"
    max_page_size = 1000


class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class GenreCreateAPIView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOnlyPermission]


class GenreRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOnlyPermission,)


class GenreUpdateAPIView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOnlyPermission]
    http_method_names = ["put"]


class GenreDestroyAPIView(generics.DestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOnlyPermission,)


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


class SongListAPIView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongRetrieveSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination


class SongCreateAPIView(generics.CreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer
    permission_classes = [IsAdminOnlyPermission]


class SongRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongRetrieveSerializer
    permission_classes = (IsAdminOnlyPermission,)


class SongUpdateAPIView(generics.UpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongCreateSerializer
    permission_classes = [IsAdminOnlyPermission]
    http_method_names = ["put"]


class SongDestroyAPIView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongRetrieveSerializer
    permission_classes = (IsAdminOnlyPermission,)
