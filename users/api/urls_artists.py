from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArtistListCreateAPIView.as_view()),
    path("<int:pk>/", views.ArtistRetrieveAPIView.as_view()),
    path("<int:pk>/", views.ArtistUpdateAPIView.as_view()),
    path("<int:pk>/", views.ArtistDestroyAPIView.as_view()),
]
