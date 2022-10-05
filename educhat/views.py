from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')
    # return HttpResponse("This is chat page")