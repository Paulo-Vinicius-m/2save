from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'api'
urlpatterns = [
    path('restaurantes', views.view_restaurantes.as_view(), name='restaurantes'),
    path('restaurante/pedidos', views.view_pedidos_restaurante.as_view(), name='restaurante-pedidos'),
    path('customer/pedidos', views.view_pedidos_customer.as_view(), name='customer-pedidos'),
    path('carrinho', views.view_carrinho.as_view(), name='carrinho'),
    path('alterar-cardapio', views.view_produtos.as_view(), name='alterar-cardapio'),
]
