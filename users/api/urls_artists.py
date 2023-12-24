from django.urls import path

from . import views

urlpatterns = [
    path("songs/<int:pk>/", views.ArtistSongsListAPIView.as_view()),
    path("", views.ArtistListCreateAPIView.as_view()),
    path("<int:pk>/", views.ArtistRetrieveUpdateDestroyAPIView.as_view()),
]
