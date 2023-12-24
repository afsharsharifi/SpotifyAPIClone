from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserListCreateAPIView.as_view()),
    path("<int:pk>/", views.UserRetrieveUpdateDestroyAPIView.as_view()),
]
