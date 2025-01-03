from django.http import JsonResponse, HttpResponse
from settings.settings import SECRET_KEY
import jwt

def autorize(function):
    def wrapper(*args, **kwargs) -> HttpResponse:
        try:
            token = args[0].COOKIES.get('Authorization')
            payload = jwt.decode(token, key=SECRET_KEY, algorithms='HS256')
        except Exception as e:
            return JsonResponse({'error': e}, status=401)
        
        return function(*args, **kwargs)
    
    return wrapper