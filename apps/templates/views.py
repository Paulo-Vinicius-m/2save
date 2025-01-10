from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from users.utils import autorize
from settings.settings import SECRET_KEY
import jwt

# Create your views here.
#@ensure_csrf_cookie
def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'cadastro.html')

def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

@autorize(perm='customer')
def home(request: HttpRequest) -> HttpResponse:
    username = request.COOKIES.get('Authorization')
    username = jwt.decode(username, key=SECRET_KEY, algorithms='HS256')['name']
    return HttpResponse('Bem vindo ' + username + '!')

def inicio(request: HttpRequest) -> HttpResponse:
    return render(request, 'tela-inicial.html')

#@autorize('customer')
def pagamento(request: HttpRequest) -> HttpResponse:
    return render(request, 'pagamento.html')

#@autorize('customer')
def c_perfil(request: HttpRequest) -> HttpResponse:
    return render(request, 'perfil-cliente.html')

#@autorize('restaurant')
def r_perfil(request: HttpRequest) -> HttpResponse:
    return render(request, 'perfil-restaurante.html')

#@autorize('restaurant')
def r_cardapio(request: HttpRequest) -> HttpResponse:
    return render(request, 'cardapio-restaurante.html')

#@autorize
def pedidos(request: HttpRequest) -> HttpResponse:
    return render(request, 'pedidos.html')

#@autorize
def c_cardapio(request: HttpRequest, id: int) -> HttpResponse:
    return render(request, 'cardapio-cliente.html')

#@autorize
def buscar(request: HttpRequest) -> HttpResponse:
    return render(request, 'buscar.html')