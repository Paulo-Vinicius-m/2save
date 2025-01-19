from django.contrib import admin
from .models import Restaurante, Consumidor, Produto, Carrinho, Pedido


# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Consumidor)
admin.site.register(Produto)
admin.site.register(Carrinho)
admin.site.register(Pedido)