from django.urls import path
from .views import Index, Splash, Profile

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('login/',Splash.as_view(),name='login'),
    path('profile/<slug:pk>/',Profile.as_view(),name='profile'),
]