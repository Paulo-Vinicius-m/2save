from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'templates'
urlpatterns = [
    path('register', views.register, name='register'),
    path('home', views.home, name='home'),
]