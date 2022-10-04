from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
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
    
    def post(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)
        qtdForm = QtdForm(self.request.POST)
        if qtdForm.is_valid():
            self.request.session['cart'][qtdForm['id'].value()]={
                'id':qtdForm['id'].value(),
                'quantidade':qtdForm['quantidade'].value()}
            url = reverse(viewname='home', kwargs={'result': 'sucesso'})
            return HttpResponseRedirect(url)
        else:
            url = reverse(viewname='home', kwargs={'result': 'erro'})
            return HttpResponseRedirect(url)
    
