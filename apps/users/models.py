from django.db import models
from django.contrib.auth.models import User
from settings.settings import SECRET_KEY
import jwt


class Restaurante(User):
    logo = models.ImageField(upload_to='logos/', blank=True)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11, blank=True)

    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    
    def generate_token(self) -> str:
        return jwt.encode(payload={'sub': str(self.id), 'name': self.username, 'class': 'restaurant'}, key=SECRET_KEY, algorithm='HS256')


    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'


class Consumidor(User):
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, blank=True)

    estado = models.CharField(max_length=2)
    cidade = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username
    
    def generate_token(self) -> str:
        return jwt.encode(payload={'sub': str(self.id), 'name': self.username, 'class': 'customer'}, key=SECRET_KEY, algorithm='HS256')

    class Meta:
        verbose_name = 'Consumidor'
        verbose_name_plural = 'Consumidores'
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('prato', 'Prato'), ('bebida', 'Bebida')], default='prato')
    
    def __str__(self):
        return self.nome

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


class Pedido(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    preco = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    data = models.DateTimeField(auto_now_add=True)
    aceito = models.BooleanField(default=False)
    entregue = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.consumidor.username} - {self.data}'
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def to_dict(self) -> dict:
        return {
            'consumidor': self.consumidor.username,
            'produtos': self.produtos_serializer(),
            'data': self.data,
            'entregue': self.entregue,
        }
    
    def save(self, *args, **kwargs):

        # Calcula o preço total do pedido
        self.preco = 0
        for produto in self.produtos.all():
            self.preco += produto.preco

        # Verifica se todos os produtos são do mesmo restaurante
        if len(set([produto.restaurante for produto in self.produtos.all()])) > 1:
            raise ValueError('Todos os produtos devem ser do mesmo restaurante')
        else:
            self.restaurante = self.produtos.first().restaurante

        super().save(*args, **kwargs)
