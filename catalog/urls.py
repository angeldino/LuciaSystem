from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('consultas/', views.consultas, name="consultas"),
    path('capturas/', views.capturas, name="capturas")
]