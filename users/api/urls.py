from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view()),
    path("<int:pk>/", views.UserRetrieveAPIView.as_view()),
    path("<int:pk>/", views.UserUpdateAPIView.as_view()),
    path("<int:pk>/", views.UserDestroyAPIView.as_view()),
]
