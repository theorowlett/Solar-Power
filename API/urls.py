from django.urls import path
from .views import DetailUser, ListUser, CreateUser

urlpatterns = [
    path('',ListUser.as_view()),
    path('<int:pk>/',DetailUser.as_view()),
    path('new/',CreateUser.as_view()),
]
