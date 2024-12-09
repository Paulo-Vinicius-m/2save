from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.contrib.auth.models import User
from settings.settings import SECRET_KEY
import jwt

# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    name = request.POST['name']
    password = request.POST['password']
    email1 = request.POST['email1']
    email2 = request.POST['email2']
    
    if len(name) not in range(4, 20):
        return JsonResponse({'error': 'Invalid name length'}, status=400)
    
    if len(password) > 25:
        return JsonResponse({'error': 'Invalid password length'}, status=400)
    
    if email1 != email2:
        return JsonResponse({'error': "emails don't match"}, status=400)
    
    # TODO - verify if it's a valid email

    user = User.objects.create_user(
        username=request.POST['name'],
        email=request.POST['email1'],
        password=request.POST['password']
    )

    jwt.encode(payload={'sub': user.id, 'name': user.username, 'class': 'consumer'},key=SECRET_KEY, algorithm='HS256')
    return JsonResponse({'message': 'User created'}, status=201)