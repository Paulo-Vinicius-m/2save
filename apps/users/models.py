from django.db import models
from django.contrib.auth.models import User
from settings.settings import SECRET_KEY
import jwt


class Restaurante(User):
    logo = models.ImageField(upload_to='logos/', blank=True)
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=11, blank=True)
    descricao = models.TextField(blank=True)
    pix = models.CharField(max_length=20, blank=True)
    imagem = models.ImageField(upload_to='restaurantes/', blank=True, null=True)

    endereco = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    def generate_token(self) -> str:
        return jwt.encode(payload={'sub': str(self.id), 'name': self.username, 'class': 'restaurant'}, key=SECRET_KEY, algorithm='HS256')

    def to_dict(self) -> dict:
        return {
            'username': self.username,
                'id': self.id,
                'cnpj': self.cnpj,
                'email': self.email,
                'telefone': self.telefone,
                'imagem': self.imagem.url if self.imagem else None,
                'endereco': self.endereco,
                'descricao': self.descricao,
                'pix': self.pix,
                'pratos': produto_serializer(Produto.objects.filter(restaurante=self, tipo='prato')),
                'bebidas': produto_serializer(Produto.objects.filter(restaurante=self, tipo='bebida')),
        }
    
    class Meta:
        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'


class Consumidor(User):
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=11, blank=True)

    endereco = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    
    def generate_token(self) -> str:
        return jwt.encode(payload={'sub': str(self.id), 'name': self.username, 'class': 'customer'}, key=SECRET_KEY, algorithm='HS256')

    def to_dict(self) -> dict:
        return {
            'nome': self.username,
            'id': self.id,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'endereco': self.endereco,
        }

    class Meta:
        verbose_name = 'Consumidor'
        verbose_name_plural = 'Consumidores'
    
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', blank=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('prato', 'Prato'), ('bebida', 'Bebida')], default='prato')
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'tipo': self.tipo,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': str(self.preco),
            'imagem': self.imagem.url if self.imagem else None,
        }

    def __str__(self):
        return self.nome

def produto_serializer(produtos: models.QuerySet) -> dict:
    return [produto.to_dict() for produto in produtos]

class Carrinho(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE, unique=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, blank=True, null=True)
    produtos = models.ManyToManyField(Produto)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def to_dict(self) -> dict:
        return {
            'consumidor': self.consumidor.id,
            'restaurante': self.restaurante.id if self.restaurante else None,
            'produtos': produto_serializer(self.produtos.get_queryset()),
        }
    
    def save(self, *args, **kwargs):

        if self.pk is not None:
            # Calcula o preço total do pedido
            self.preco = 0
            for produto in self.produtos.all():
                self.preco += produto.preco
            

            # Verifica se todos os produtos são do mesmo restaurante
            if self.produtos.count() == 0:
                pass
            elif len(set([produto.restaurante for produto in self.produtos.all()])) > 1:
                raise ValueError('Todos os produtos devem ser do mesmo restaurante')
            else:
                self.restaurante = self.produtos.first().restaurante

        super().save(*args, **kwargs)


class Pedido(models.Model):
    consumidor = models.ForeignKey(Consumidor, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, blank=True)
    produtos = models.ManyToManyField(Produto)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
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
            'id': self.id,
            'consumidor': self.consumidor.id,
            'restaurante': self.restaurante.id if self.restaurante else None,
            'produtos': produto_serializer(self.produtos.get_queryset()),
            'data': self.data,
            'aceito': self.aceito,
            'entregue': self.entregue,
        }
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            # Calcula o preço total do pedido
            self.preco = 0
            for produto in self.produtos.all():
                self.preco += produto.preco
            
            # Verifica se todos os produtos são do mesmo restaurante
            if self.produtos.count() == 0:
                pass
            elif len(set([produto.restaurante for produto in self.produtos.all()])) > 1:
                raise ValueError('Todos os produtos devem ser do mesmo restaurante')
            else:
                self.restaurante = self.produtos.first().restaurante

        super().save(*args, **kwargs)

'''class PedidoProduto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return f'{self.pedido.consumidor.username} - {self.produto.nome}'

    class Meta:
        verbose_name = 'Pedido Produto'
        verbose_name_plural = 'Pedidos Produtos'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)'''