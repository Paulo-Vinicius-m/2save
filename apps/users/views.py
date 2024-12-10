from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from settings.settings import SECRET_KEY
from django.contrib.auth.models import User
from users.models import Restaurante, Consumidor
from django.core.serializers import serialize
import jwt
from .utils import autorize


def register(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    name = request.POST['name']
    password = request.POST['password']
    email1 = request.POST['email']
    email2 = request.POST['email2']
    tipo = request.POST['tipo']
    identificador = request.POST['identificador']
    
    if len(name) not in range(4, 20):
        return JsonResponse({'error': 'Invalid name length'}, status=400)
    
    if len(password) > 25:
        return JsonResponse({'error': 'Invalid password length'}, status=400)
    
    if email1 != email2:
        return JsonResponse({'error': "emails don't match"}, status=400)
    
    # TODO - verify if it's a valid email

    if tipo == 'R':
        user = Restaurante.objects.create_user(
            username=name,
            email=email1,
            password=password,
            cnpj=identificador
        )
    elif tipo == 'C':
        user = Consumidor.objects.create_user(
            username=name,
            email=email1,
            password=password,
            cpf=identificador
        )

    token = jwt.encode(payload={'sub': str(user.id), 'name': user.username, 'class': 'consumer'}, key=SECRET_KEY, algorithm='HS256')
    return JsonResponse({'message': 'User created', 'token': token}, status=201)

def login(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    email = request.POST['email']
    password = request.POST['password']
    
    user = User.objects.get(email=email)
    
    if user.check_password(password):
        token = jwt.encode(payload={'sub': str(user.id), 'name': user.username, 'class': 'consumer'},key=SECRET_KEY, algorithm='HS256')
        return JsonResponse({'message': 'User logged in', 'token': token})


