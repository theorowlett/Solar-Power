from django.urls import path
from .views import Index, Splash

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('login/',Splash.as_view(),name='login')
]