from django.contrib import admin
from .models import Restaurante, Consumidor, Prato, Bebida


# Register your models here.
admin.site.register(Restaurante)
admin.site.register(Consumidor)
admin.site.register(Prato)
admin.site.register(Bebida)