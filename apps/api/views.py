from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from users.models import Restaurante, Consumidor, Prato, Bebida, produto_serializer
from django.core.serializers import serialize
from django.forms.models import model_to_dict
from users.utils import autorize
from django.contrib.auth.models import User

# Create your views here.
@autorize('customer') 
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
                'pratos': produto_serializer(Prato.objects.filter(restaurante=restautante)),
                'bebidas': produto_serializer(Bebida.objects.filter(restaurante=restautante)),
            }
            for restautante in Restaurante.objects.filter(username__icontains=name)
        ]
        
        return JsonResponse(
            data=restaurantes,
            status=200,
            safe=False,
        )

    return HttpResponse(status=405)