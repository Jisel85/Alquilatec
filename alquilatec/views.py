import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, 'index.html', context)

@login_required(login_url='/')
def contacto(request):
    context = {}
    return render(request, 'contacto.html', context)

@login_required(login_url='/')
def equipos(request):
    context = {}
    return render(request, 'equipos.html', context)

@login_required(login_url='/')
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

def acceder(request):
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    user = User.objects.filter(email=email).first()
    if not user:
        raise Exception('Usuario no existe')
    user = authenticate(request, username=user.username, password=password)
    if not user:
        raise Exception('Contraseña invalida')
    login(request, user)
    return JsonResponse({'status':'ok'})

def salir(request):
    logout(request)
    return redirect('/')
