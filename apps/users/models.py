from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurante(User):
    logo = models.ImageField(upload_to='logos/', blank=True)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11, blank=True)

    '''estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)'''
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'


class Consumidor(User):
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, blank=True)

    '''estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    '''
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Consumidor'
        verbose_name_plural = 'Consumidores'
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        abstract = True

def produto_serializer(produtos: models.QuerySet) -> dict:
    return [
        {
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': str(produto.preco),
            'imagem': produto.imagem.url if produto.imagem else None,
        }
        for produto in produtos
    ]


class Prato(Produto):
    pass

class Bebida(Produto):
    pass