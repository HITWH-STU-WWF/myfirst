from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.index),
    path('temp/',views.home_temp)
]