from django.test import TestCase
from django.contrib.auth.models import User
from .models import Restaurante, Consumidor, Produto, Carrinho, Pedido, Pedido_Produto
from settings.settings import SECRET_KEY
import jwt

class RestauranteModelTest(TestCase):
    def setUp(self):
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            estado='RN',
            cidade='Natal',
            endereco='Rua A',
            numero='123'
        )

    def test_restaurante_creation(self):
        self.assertEqual(self.restaurante.username, 'restaurante1')
        self.assertEqual(self.restaurante.cnpj, '12345678901234')

    def test_generate_token(self):
        token = self.restaurante.generate_token()
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded['sub'], str(self.restaurante.id))
        self.assertEqual(decoded['name'], self.restaurante.username)
        self.assertEqual(decoded['class'], 'restaurant')


class ConsumidorModelTest(TestCase):
    def setUp(self):
        self.consumidor = Consumidor.objects.create_user(
            username='consumidor1',
            password='password123',
            cpf='12345678901',
            estado='RN',
            cidade='Natal',
            endereco='Rua B',
            numero='456'
        )

    def test_consumidor_creation(self):
        self.assertEqual(self.consumidor.username, 'consumidor1')
        self.assertEqual(self.consumidor.cpf, '12345678901')

    def test_generate_token(self):
        token = self.consumidor.generate_token()
        decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded['sub'], str(self.consumidor.id))
        self.assertEqual(decoded['name'], self.consumidor.username)
        self.assertEqual(decoded['class'], 'customer')


class ProdutoModelTest(TestCase):
    def setUp(self):
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            estado='RN',
            cidade='Natal',
            endereco='Rua A',
            numero='123'
        )
        self.produto = Produto.objects.create(
            nome='Produto1',
            descricao='Descricao do produto',
            preco=10.50,
            restaurante=self.restaurante,
            tipo='prato'
        )

    def test_produto_creation(self):
        self.assertEqual(self.produto.nome, 'Produto1')
        self.assertEqual(self.produto.descricao, 'Descricao do produto')
        self.assertEqual(self.produto.preco, 10.50)
        self.assertEqual(self.produto.restaurante, self.restaurante)


class CarrinhoModelTest(TestCase):
    def setUp(self):
        self.consumidor = Consumidor.objects.create_user(
            username='consumidor1',
            password='password123',
            cpf='12345678901',
            estado='RN',
            cidade='Natal',
            endereco='Rua B',
            numero='456'
        )
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            estado='RN',
            cidade='Natal',
            endereco='Rua A',
            numero='123'
        )
        self.produto = Produto.objects.create(
            nome='Produto1',
            descricao='Descricao do produto',
            preco=10.50,
            restaurante=self.restaurante,
            tipo='prato'
        )
        self.carrinho = Carrinho.objects.create(
            consumidor=self.consumidor,
            restaurante=self.restaurante
        )
        self.carrinho.produtos.add(self.produto)
        self.carrinho.save()

    def test_carrinho_creation(self):
        self.assertEqual(self.carrinho.consumidor, self.consumidor)
        self.assertEqual(self.carrinho.restaurante, self.restaurante)
        self.assertEqual(self.carrinho.produtos.count(), 1)
        self.assertEqual(self.carrinho.preco, 10.50)


class PedidoModelTest(TestCase):
    def setUp(self):
        self.consumidor = Consumidor.objects.create_user(
            username='consumidor1',
            password='password123',
            cpf='12345678901',
            estado='RN',
            cidade='Natal',
            endereco='Rua B',
            numero='456'
        )
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            estado='RN',
            cidade='Natal',
            endereco='Rua A',
            numero='123'
        )
        self.produto = Produto.objects.create(
            nome='Produto1',
            descricao='Descricao do produto',
            preco=10.50,
            restaurante=self.restaurante,
            tipo='prato'
        )
        self.pedido = Pedido.objects.create(
            consumidor=self.consumidor,
            restaurante=self.restaurante
        )
        self.pedido.produtos.add(self.produto)
        self.pedido.save()

    def test_pedido_creation(self):
        self.assertEqual(self.pedido.consumidor, self.consumidor)
        self.assertEqual(self.pedido.restaurante, self.restaurante)
        self.assertEqual(self.pedido.produtos.count(), 1)
        self.assertEqual(self.pedido.preco, 10.50)


'''class PedidoProdutoModelTest(TestCase):
    def setUp(self):
        self.consumidor = Consumidor.objects.create_user(
            username='consumidor1',
            password='password123',
            cpf='12345678901',
            estado='RN',
            cidade='Natal',
            endereco='Rua B',
            numero='456'
        )
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            estado='RN',
            cidade='Natal',
            endereco='Rua A',
            numero='123'
        )
        self.produto = Produto.objects.create(
            nome='Produto1',
            descricao='Descricao do produto',
            preco=10.50,
            restaurante=self.restaurante,
            tipo='prato'
        )
        self.pedido = Pedido.objects.create(
            consumidor=self.consumidor,
            restaurante=self.restaurante
        )
        self.pedido.produtos.add(self.produto)
        self.pedido.save()
        self.pedido_produto = Pedido_Produto.objects.create(
            pedido=self.pedido,
            produto=self.produto,
            quantidade=2
        )

    def test_pedido_produto_creation(self):
        self.assertEqual(self.pedido_produto.pedido, self.pedido)
        self.assertEqual(self.pedido_produto.produto, self.produto)
        self.assertEqual(self.pedido_produto.quantidade, 2)'''