from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from .forms import QtdForm
from .models import Item
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def sobre(request):
    return render(request,'firn/sobre.html')

class HomeListView(ListView):
    model = Item
    
    def get_context_data(self, **kwargs):
        context=super(HomeListView,self).get_context_data(**kwargs)
        context['result'] = self.request.GET.get('result', '') # default to empty string if not in GET data
        context['carr'] = len(self.request.session.items())
        context['form']=QtdForm()
        return context

    def post(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)
        qtdForm = QtdForm(self.request.POST)
        if qtdForm.is_valid():
            self.request.session[qtdForm['id'].value()]={
                'id':qtdForm['id'].value(),
                'quantidade':qtdForm['quantidade'].value()}
            return HttpResponseRedirect("?result=sucesso")
        else:
            return HttpResponseRedirect("?result=erro")
    
class LojaListView(ListView):
    paginate_by = 12
    model = Item
    
    def post(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)
        qtdForm = QtdForm(self.request.POST)
        if qtdForm.is_valid():
            self.request.session[qtdForm['id'].value()]={
                'id':qtdForm['id'].value(),
                'quantidade':qtdForm['quantidade'].value()}
            return HttpResponseRedirect("?result=sucesso")
        else:
            return HttpResponseRedirect("?result=erro")
    
    def get_context_data(self, **kwargs):
        context=super(LojaListView,self).get_context_data(**kwargs)
        context['form']=QtdForm()
        context['result'] = self.request.GET.get('result', '')
        context['carr'] = len(self.request.session.items())
        return context

class CartListView(ListView):
    model = Item
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carr"] = len(self.request.session.items())
        context["cart"] = self.request.session.items()
        return context

    def get_queryset(self):
        queryset=Item.objects.filter(id__in=list(self.request.session.keys())),
        return queryset[0]
    