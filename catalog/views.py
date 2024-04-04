from django.shortcuts import render
from .models import *
from django.urls import include, path

# Create your views here.
def index(request):
    return render(request, 'index.html')

def consultas(request):
    users = User.objects.all()
    return render(request, 'consultas.html', {'users': users})

def capturas(request):
    return render(request, 'capturas.html')