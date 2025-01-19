from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from users.models import Restaurante, Consumidor, Produto, produto_serializer, Pedido, Carrinho
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from users.utils import autorize
from django.contrib.auth.models import User
from django.views.generic import View
import json

# Create your views here.
'''@autorize('customer or restaurant') 
def restaurantes(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        # Busca por nome de restaurante

        name = request.GET.get('username', default='')
        restaurantes = [
            {
                'username': restautante.username,
                'cnpj': restautante.cnpj,
                'email': restautante.email,
                'telefone': restautante.telefone,
                'logo': restautante.logo.url if restautante.logo else None,
                'pratos': produto_serializer(Produto.objects.filter(restaurante=restautante, tipo='prato')),
                'bebidas': produto_serializer(Produto.objects.filter(restaurante=restautante, tipo='bebida')),
            }
            for restautante in Restaurante.objects.filter(username__icontains=name)
        ]
        
        return JsonResponse(
            data=restaurantes,
            status=200,
            safe=False,
        )

    return HttpResponse(status=405)'''

class view_restaurantes(View):
    @autorize()
    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Busca por nome de restaurante

        name = request.GET.get('username', default='')
        restaurantes = [
            {
                'username': restautante.username,
                'cnpj': restautante.cnpj,
                'email': restautante.email,
                'telefone': restautante.telefone,
                'logo': restautante.logo.url if restautante.logo else None,
                'pratos': produto_serializer(Produto.objects.filter(restaurante=restautante, tipo='prato')),
                'bebidas': produto_serializer(Produto.objects.filter(restaurante=restautante, tipo='bebida')),
            }
            for restautante in Restaurante.objects.filter(username__icontains=name)
        ]
        
        return JsonResponse(
            data=restaurantes,
            status=200,
            safe=False,
        )

    def put(self, request: HttpRequest) -> HttpResponse:
        # Atualiza um restaurante

        data = request.body.decode('utf-8')
        restaurante = Restaurante.objects.get(username=data.get('username'))
        restaurante.email = data.get('email')
        restaurante.cnpj = data.get('cnpj')
        restaurante.telefone = data.get('telefone')
        restaurante.estado = data.get('estado')
        restaurante.cidade = data.get('cidade')
        restaurante.endereco = data.get('endereco')
        restaurante.numero = data.get('numero')
        restaurante.set_password(data.get('password'))
        restaurante.save()
        
        return JsonResponse(
            data=model_to_dict(restaurante),
            status=200,
            safe=False,
        )


class view_pedidos(View):

    @autorize('customer')
    def post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Cria um pedido

        data = request.body.decode('utf-8')
        consumidor = Consumidor.objects.get(id=kwargs['token']['sub'])
        produtos = Produto.objects.filter(id__in=data.get('produtos'))
        pedido = Pedido.objects.create(consumidor=consumidor)
        pedido.produtos.set(produtos)
        
        return JsonResponse(
            data=model_to_dict(pedido),
            status=201,
            safe=False,
        )
    
    @autorize('restaurant')
    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Busca por pedidos

        pedidos = Pedido.objects.filter(restaurante__id=kwargs['token']['sub'])
        return JsonResponse(
            data=[pedido.to_dict() for pedido in pedidos],
            status=200,
            safe=False,
        )
    
class view_carrinho(View):
    @autorize('customer')
    def get(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Busca por carrinho

        try:
            carrinho = Carrinho.objects.get(consumidor__id=kwargs['token']['sub'])
        except Carrinho.DoesNotExist:
            carrinho = Carrinho.objects.create(consumidor=Consumidor.objects.get(id=kwargs['token']['sub']))

        return JsonResponse(
            data=carrinho.to_dict(),
            status=200,
            safe=False,
        )
    
    @autorize('customer')
    def put(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Atualiza o carrinho

        data = request.body.decode('utf-8')
        carrinho = Carrinho.objects.get(consumidor__id=kwargs['token']['sub'])
        produtos = Produto.objects.filter(id__in=data.get('produtos'))
        carrinho.produtos.set(produtos, clear=True)
        
        return JsonResponse(
            data=carrinho.to_dict(),
            status=200,
            safe=False,
        )

# /api/alterar-cardapio/
class view_produtos(View):
    @autorize('restaurant')
    def post(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Cria um produto

        data = json.loads(request.body.decode('utf-8'))
        restaurante = Restaurante.objects.get(id=kwargs['token']['sub'])
        produto = Produto.objects.create(
            nome=data.get('nome'),
            descricao=data.get('descricao'),
            preco=data.get('preco'),
            imagem=data.get('imagem'),
            tipo=data.get('tipo'),
            restaurante=restaurante,
        )
        
        return JsonResponse(
            data=produto.to_dict(),
            status=201,
            safe=False,
        )
    
    @autorize('restaurant')
    def put(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Atualiza um produto

        data = json.loads(request.body.decode('utf-8'))
        produto = Produto.objects.get(restaurante = kwargs['token']['sub'], id=data.get('id'))
        produto.nome = data.get('nome')
        produto.descricao = data.get('descricao')
        produto.preco = data.get('preco')
        produto.imagem = data.get('imagem')
        produto.tipo = data.get('tipo')
        produto.save()
        
        return JsonResponse(
            data=produto.to_dict(),
            status=200,
            safe=False,
        )
    
    @autorize('restaurant')
    def delete(self, request: HttpRequest, **kwargs) -> HttpResponse:
        # Deleta um produto

        data = json.loads(request.body.decode('utf-8'))
        produto = Produto.objects.get(restaurante = kwargs['token']['sub'], id=data.get('id'))
        produto.delete()
        
        return HttpResponse(
            content='Produto deletado',
            status=200
        )