from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('restaurantes', views.view_restaurantes.as_view(), name='restaurantes'),
    path('pedidos', views.view_pedidos.as_view(), name='pedidos'),
]
