from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from users.utils import autorize
from settings.settings import SECRET_KEY
import jwt

# Create your views here.
#@ensure_csrf_cookie
def register(request: HttpRequest) -> HttpResponse:
    return HttpResponse('ola')

@autorize
def home(request: HttpRequest) -> HttpResponse:
    username = request.headers.get('Authorization').split(' ')[1]
    username = jwt.decode(username, key=SECRET_KEY, algorithms='HS256')['name']
    return HttpResponse('Bem vindo ' + username + '!')