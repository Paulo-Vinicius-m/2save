from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'templates'
urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('home', views.home, name='home'),
    path('inicio', views.inicio, name='inicio'),
    path('pagamento', views.pagamento, name='pagamento'),
    path('cliente/perfil', views.c_perfil, name='cperfil'),
    path('restaurante/perfil', views.r_perfil, name='rperfil'),
    path('meu-cardapio', views.r_cardapio, name='r_cardapio'),
    path('meus-pedidos', views.pedidos, name='pedidos'),
    path('oi', views.c_cardapio, name='c_cardapio'),
    path('buscar', views.buscar, name='buscar'),
]