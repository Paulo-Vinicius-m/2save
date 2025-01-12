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
        return JsonResponse({'error': 'Invalid name length'}, status=400)
    
    if len(password) > 25:
        return JsonResponse({'error': 'Invalid password length'}, status=400)
    
    if email1 != email2:
        return JsonResponse({'error': "emails don't match"}, status=400)
    
    # TODO - verify if it's a valid email

    if User.objects.filter(username=name) or User.objects.filter(email=email1):
        return JsonResponse({'error': 'User already exists'}, status=400)
    
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

    token = jwt.encode(payload={'sub': str(user.id), 'name': user.username, 'class': 'customer'}, key=SECRET_KEY, algorithm='HS256')
    #return JsonResponse({'message': 'User created', 'token': token}, status=201)
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
        token = jwt.encode(payload={'sub': str(user.id), 'name': user.username, 'class': 'customer'},key=SECRET_KEY, algorithm='HS256')
        response = JsonResponse({'message': 'User authenticated', 'token': token}, status=200)
        response.set_cookie('Authorization', token, httponly=True, samesite='Strict')
        return response
    else:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)


