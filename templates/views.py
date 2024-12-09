from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
#@ensure_csrf_cookie
def register(request):
    return HttpResponse('ola')