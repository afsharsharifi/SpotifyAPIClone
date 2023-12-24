from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArtistListCreateAPIView.as_view()),
    path("<int:pk>/", views.ArtistRetrieveUpdateDestroyAPIView.as_view()),
]
