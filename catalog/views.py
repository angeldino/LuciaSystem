from django.shortcuts import render
from django.urls import include

# Create your views here.
def index(request):
    return render(request, include('index.html'))