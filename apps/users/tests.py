from django.test import TestCase
from django.contrib.auth.models import User
from .models import Restaurante, Consumidor, Produto, Carrinho, Pedido
from settings.settings import SECRET_KEY
import jwt
from django.core.files.uploadedfile import SimpleUploadedFile

class RestauranteModelTest(TestCase):
    def setUp(self):
        self.maxDiff = None
        self.restaurante = Restaurante.objects.create_user(
            username='test_restaurant',
            password='password123',
            cnpj='12345678901234',
            telefone='12345678901',
            endereco='Rua Teste',
            pix='12345678901',
            imagem=SimpleUploadedFile(name='test_image.jpg', content=b'oi', content_type='image/jpeg'),
            descricao='Descricao Teste',
        )

    def test_restaurante_creation(self):
        self.assertIsInstance(self.restaurante, Restaurante)
        self.assertEqual(self.restaurante.username, 'test_restaurant')
        self.assertEqual(self.restaurante.cnpj, '12345678901234')
        self.assertEqual(self.restaurante.telefone, '12345678901')
        self.assertEqual(self.restaurante.endereco, 'Rua Teste')
        self.assertEqual(self.restaurante.pix, '12345678901')
        self.assertEqual(b'oi', self.restaurante.imagem.read())
        self.assertEqual(self.restaurante.descricao, 'Descricao Teste')

    def test_restaurante_str(self):
        self.assertEqual(str(self.restaurante), 'test_restaurant')

    def test_generate_token(self):
        token = self.restaurante.generate_token()
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded_token['sub'], str(self.restaurante.id))
        self.assertEqual(decoded_token['name'], self.restaurante.username)
        self.assertEqual(decoded_token['class'], 'restaurant')

    def test_to_dict(self):
        produto_prato = Produto.objects.create(
            nome='Prato Teste',
            descricao='Descricao Teste',
            preco=10.00,
            restaurante=self.restaurante,
            tipo='prato'
        )
        produto_bebida = Produto.objects.create(
            nome='Bebida Teste',
            descricao='Descricao Teste',
            preco=5.00,
            restaurante=self.restaurante,
            tipo='bebida'
        )
        expected_dict = {
            'username': self.restaurante.username,
            'id': self.restaurante.id,
            'cnpj': self.restaurante.cnpj,
            'email': self.restaurante.email,
            'telefone': self.restaurante.telefone,
            'imagem': self.restaurante.imagem.url,
            'endereco': self.restaurante.endereco,
            'descricao': self.restaurante.descricao,
            'pix': self.restaurante.pix,
            'pratos': [produto_prato.to_dict()],
            'bebidas': [produto_bebida.to_dict()],
        }
        self.assertEqual(self.restaurante.to_dict(), expected_dict)

class ConsumidorModelTest(TestCase):
    def setUp(self):
        self.consumidor = Consumidor.objects.create_user(
            username='consumidor1',
            password='password123',
            cpf='12345678901',
            endereco='Rua B',
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
            endereco='Rua A',
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
            endereco='Rua B',
        )
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            endereco='Rua A',
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
            endereco='Rua B',
        )
        self.restaurante = Restaurante.objects.create_user(
            username='restaurante1',
            password='password123',
            cnpj='12345678901234',
            endereco='Rua A',
        )
        self.produto1 = Produto.objects.create(
            nome='Produto1',
            descricao='Descricao do produto',
            preco=10.50,
            restaurante=self.restaurante,
            tipo='prato'
        )
        self.produto2 = Produto.objects.create(
            nome='Produto2',
            descricao='Descricao do produto',
            preco=11.50,
            restaurante=self.restaurante,
            tipo='prato'
        )
        self.pedido = Pedido.objects.create(
            consumidor=self.consumidor,
            restaurante=self.restaurante
        )
        self.pedido.produtos.add(self.produto1)
        self.pedido.save()

    def test_pedido_creation(self):
        self.assertEqual(self.pedido.consumidor, self.consumidor)
        self.assertEqual(self.pedido.restaurante, self.restaurante)
        self.assertEqual(self.pedido.produtos.count(), 1)
        self.assertEqual(self.pedido.preco, 10.50)

    def test_pedido_add_new_produto(self):
        self.pedido.produtos.add(self.produto2)
        self.pedido.save()
        self.assertEqual(self.pedido.produtos.count(), 2)
        self.assertEqual(self.pedido.preco, 22.00, f'{[produto.preco for produto in self.pedido.produtos.all()]}')

    '''
    Não foi implementado ainda
    def test_pedido_add_same_produto_again(self):
        self.pedido.produtos.add(self.produto1)
        self.pedido.save()
        self.assertEqual(self.pedido.produtos.count(), 2)
        self.assertEqual(self.pedido.preco, 21)'''

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