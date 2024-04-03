from django.shortcuts import render
from django.urls import include, path

# Create your views here.
def index(request):
    return render(request, 'index.html')

def consultas(request):
    return render(request, 'consultas.html')

def capturas(request):
    return render(request, 'capturas.html')