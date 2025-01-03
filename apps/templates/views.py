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

@autorize
def home(request: HttpRequest) -> HttpResponse:
    username = request.COOKIES.get('Authorization')
    username = jwt.decode(username, key=SECRET_KEY, algorithms='HS256')['name']
    return HttpResponse('Bem vindo ' + username + '!')