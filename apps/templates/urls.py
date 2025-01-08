from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'templates'
urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('inicio', views.inicio, name='inicio'),
]