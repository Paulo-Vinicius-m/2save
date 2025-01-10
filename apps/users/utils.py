from django.http import JsonResponse, HttpResponse
from settings.settings import SECRET_KEY
import jwt

def autorize(perm=''):
    def decorator(function):
        def wrapper(*args, **kwargs) -> HttpResponse:
            try:
                token = args[0].COOKIES.get('Authorization')
                payload = jwt.decode(token, key=SECRET_KEY, algorithms='HS256')
            except Exception as e:
                return HttpResponse(e, status=401)
            
            if payload['class'] not in perm:
                return HttpResponse("Você não tem permissão para acessar essa página", status=403)
            
            return function(*args, **kwargs)
        return wrapper
    return decorator

class autorizee:
    def __init__(self, perm = 'consumer'):
        self.perm = perm
    
    def __call__(self, function):
        def wrapper(*args, **kwargs) -> HttpResponse:
            try:
                token = args[0].COOKIES.get('Authorization')
                payload = jwt.decode(token, key=SECRET_KEY, algorithms='HS256')
            except Exception as e:
                return HttpResponse(e, status=401)
            
            if payload['class'] not in self.perm:
                return HttpResponse("Unauthorized: You don't have the permission to view this page", status=403)
            
            return function(*args, **kwargs)
        return wrapper