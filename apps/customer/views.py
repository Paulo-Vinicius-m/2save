from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from users.models import Restaurante, Consumidor, Produto
from django.core.serializers import serialize
from users.utils import autorize
from django.contrib.auth.models import User

# Create your views here.
@autorize    
def home(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        # Busca por nome de restaurante

        #all_objects = [*Restaurante.objects.all(), *User.objects.all()]
        name = request.GET.get('name', default='')
        restaurantes = serialize('json', Restaurante.objects,
            'username',
            'cnpj',
            'email',
            'telefone',
            'logo',
            
        )
        
        return JsonResponse(
            data=restaurantes,
            status=200,
            safe=False,
        )
