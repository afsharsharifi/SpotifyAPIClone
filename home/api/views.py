from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView, Response


class MyHomeTestAPIView(APIView):
    @extend_schema(request=None, responses=None)
    def get(self, request, format=None):
        return Response({"detail": "This is a Test Root"})
