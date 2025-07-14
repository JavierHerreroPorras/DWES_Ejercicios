from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request, 'home.html')

def home(request):
    context = {
        'message': '¡Bienvenido a la página de inicio!',
    }
    return render(request, 'home.html', context)