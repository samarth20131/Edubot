from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')

def login(request):
    return render(request, 'login.html')
    
def dashboard(request):
    return render(request, 'dashboard.html')