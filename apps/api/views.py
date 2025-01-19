from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from users.models import Restaurante, Consumidor, Produto, produto_serializer, Pedido
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from users.utils import autorize
from django.contrib.auth.models import User
from django.views.generic import View

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
    def create(self, request: HttpRequest, **kwargs) -> HttpResponse:
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