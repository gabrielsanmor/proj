from http.client import HTTPResponse
import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .forms import QtdForm
from .models import Item


# Create your views here.
def home(request):
    return render(request,'firn/home.html')

def loja(request):
    return render(request,'firn/loja.html')

def sobre(request):
    return render(request,'firn/sobre.html')

class HomeListView(ListView):
    model = Item
    
    def get_context_data(self, **kwargs):
        context=super(HomeListView,self).get_context_data(**kwargs)
        context['form']=QtdForm()
        return context
    
