from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from extensions.permissions import IsAdminOnlyPermission
from songs.api.views import StandardResultsSetPagination

from ..models import Review
from .serializers import ReviewSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminOnlyPermission]
    pagination_class = StandardResultsSetPagination


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
