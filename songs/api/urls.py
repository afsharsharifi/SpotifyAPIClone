from django.urls import path

from . import views

urlpatterns = [
    path("genre/", views.GenreListCreateAPIView.as_view()),
    path("genre/<int:pk>/", views.GenreRetrieveUpdateDestroyAPIView.as_view()),
    path("popular/", views.PopularSongsAPIView.as_view()),
    path("like/", views.LikeAPIView.as_view()),
    path("unlike/", views.UnLikeAPIView.as_view()),
    path("", views.SongListCreateAPIView.as_view()),
    path("<int:pk>/", views.SongRetrieveUpdateDestroyAPIView.as_view()),
]
