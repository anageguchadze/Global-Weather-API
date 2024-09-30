from django.urls import path
from .views import weather_api

urlpatterns = [
    path('city/<str:city>/', weather_api, name='city')
]