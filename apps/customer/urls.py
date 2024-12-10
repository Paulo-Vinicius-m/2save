from django.contrib import admin
from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('home', views.home, name='api-home'),
]