import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
    context = {}
    return render(request, 'index.html', context)

def contacto(request):
    context = {}
    return render(request, 'contacto.html', context)

def equipos(request):
    context = {}
    return render(request, 'equipos.html', context)

def principal(request):
    context = {}
    return render(request, 'principal.html', context)

def registro(request):
    context = {}
    return render(request, 'registro.html', context)

def guardar_usuario(request):
    data = json.loads(request.body)
    name = data['name']
    email = data['email']
    password = data['password']
    user = User.objects.filter(email=email).first()
    if user:
        raise Exception('Usuario existe')
    User.objects.create_user(name, email, password)
    return JsonResponse({'status':'ok'})

