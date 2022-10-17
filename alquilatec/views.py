from django.shortcuts import render


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
