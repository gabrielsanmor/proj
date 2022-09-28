from http.client import HTTPResponse
import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'firn/home.html')

def loja(request):
    return render(request,'firn/loja.html')

def sobre(request):
    return render(request,'firn/sobre.html')