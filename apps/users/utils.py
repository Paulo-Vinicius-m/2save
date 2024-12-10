from django.http import JsonResponse, HttpResponse
from settings.settings import SECRET_KEY
import jwt

def autorize(function):
    def wrapper(*args, **kwargs) -> HttpResponse:
        try:
            token = args[0].headers.get('Authorization').split(' ')[1]
            payload = jwt.decode(token, key=SECRET_KEY, algorithms='HS256')
        except Exception as e:
            return JsonResponse({'error': e}, status=401)
        
        return function(*args, payload, **kwargs)
    
    return wrapper