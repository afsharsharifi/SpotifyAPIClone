from django.urls import path

from . import views

urlpatterns = [
    path("genre/", views.GenreCreateAPIView.as_view()),
    path("genre/", views.GenreListAPIView.as_view()),
    path("genre/<int:pk>/", views.GenreRetrieveAPIView.as_view()),
    path("genre/<int:pk>/", views.GenreUpdateAPIView.as_view()),
    path("genre/<int:pk>/", views.GenreDestroyAPIView.as_view()),
    path("like/", views.LikeAPIView.as_view()),
    path("unlike/", views.UnLikeAPIView.as_view()),
    path("", views.SongCreateAPIView.as_view()),
    path("", views.SongListAPIView.as_view()),
    path("<int:pk>/", views.SongRetrieveAPIView.as_view()),
    path("<int:pk>/", views.SongUpdateAPIView.as_view()),
    path("<int:pk>/", views.SongDestroyAPIView.as_view()),
]
