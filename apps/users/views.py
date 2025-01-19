from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from settings.settings import SECRET_KEY
from django.contrib.auth.models import User
from users.models import Restaurante, Consumidor
from django.core.serializers import serialize
import jwt
from .utils import autorize
import json


def register(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    ### Checa se o payload é um JSON ou um POST
    if request.POST.__len__() == 0:
        payload = json.loads(request.body.decode('utf-8'))
    else:
        payload = request.POST

    name = payload['name']
    password = payload['password']
    email1 = payload['email']
    email2 = payload['email2']
    tipo = payload['tipo']
    identificador = payload['identificador']
    
    if len(name) not in range(4, 20):
        return HttpResponse(status=400, content='Name must be between 4 and 20 characters')
    
    if len(password) > 25:
        return HttpResponse(status=400, content='Password too long')
    
    if email1 != email2:
        return HttpResponse(status=400, content='Emails do not match')
    
    # TODO - verify if it's a valid email

    if User.objects.filter(username=name) or User.objects.filter(email=email1):
        return HttpResponse(status=400, content='User already exists')
    
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
    else:
        return HttpResponse(status=400, content='Invalid user type')

    token = user.generate_token()
    response = JsonResponse({'message': 'User created', 'token': token}, status=201)
    response.set_cookie('Authorization', token, httponly=True, samesite='Strict')
    return response

def login(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    ### Checa se o payload é um JSON ou um POST
    if request.POST.__len__() == 0:
        payload = json.loads(request.body.decode('utf-8'))
    else:
        payload = request.POST
        
    email = payload['email']
    password = payload['password']
    
    user = User.objects.get(email=email)
    
    if user.check_password(password):
        if Restaurante.objects.filter(id=user.id):
            user = Restaurante.objects.get(id=user.id)
        elif Consumidor.objects.filter(id=user.id):
            user = Consumidor.objects.get(id=user.id)
        else:
            return HttpResponse(status=500, content='Usuário inválido')
        
        token = user.generate_token()
        response = JsonResponse({'message': 'User authenticated', 'token': token}, status=200)
        response.set_cookie('Authorization', token, httponly=True, samesite='Strict')
        return response
    else:
        return HttpResponse(status=401, content='Invalid credentials')


