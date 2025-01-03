from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from users.models import Restaurante, Consumidor, Produto
from django.core.serializers import serialize
from users.utils import autorize

# Create your views here.
@autorize    
def home(request: HttpRequest, payload: dict) -> HttpResponse:
    if request.method == 'GET':
        # Busca por nome de restaurante

        name = request.GET.get('name', default='')
        restaurantes = serialize(
            format='json', 
            queryset=Restaurante.objects.filter(username__icontains=name)
        )
        
        return JsonResponse(
            data=restaurantes,
            status=200,
            safe=False,
        )
