from django.http import JsonResponse, HttpResponse
from settings.settings import SECRET_KEY
import jwt

def autorize(perm='customer or restaurant'):
    def decorator(function):
        def wrapper(*args, **kwargs) -> HttpResponse:
            try:
                token = args[1].COOKIES.get('Authorization')
                payload = jwt.decode(token, key=SECRET_KEY, algorithms='HS256')
            except Exception as e:
                return HttpResponse(e, status=401)
            
            if payload['class'] not in perm:
                return HttpResponse("Você não tem permissão para acessar essa página", status=403)
            
            kwargs['token'] = payload
            return function(*args, **kwargs)
        return wrapper
    return decorator