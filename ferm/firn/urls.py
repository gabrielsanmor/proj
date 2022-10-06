from re import template
from django.urls import path
from . import views
from .models import Item
from django.conf import settings
from django.db.models import Avg
from django.conf.urls.static import static

home_list_view= views.HomeListView.as_view(
    queryset={'itens_hp':Item.objects.filter(categoria__nome="Higiene Pessoal").annotate(av=Avg('avaliacao__nota'))[:5],
              'itens_ca':Item.objects.filter(categoria__nome="Cosmeticos")[:5],
              'itens_me':Item.objects.filter(categoria__nome="Medicamentos")[:5],
              'itens_fi':Item.objects.filter(categoria__nome="Fitness")[:5]}.items(),
    context_object_name="itens",
    template_name="firn/home.html"
)

loja_list_view = views.LojaListView.as_view(
    queryset=Item.objects.all(),
    context_object_name='itens',
    template_name='firn/loja.html'
)

cart_list_view = views.CartListView.as_view(
    context_object_name='itens',
    template_name='firn/cart.html'
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("loja", loja_list_view, name="loja"),
    path("sobre", views.sobre, name="sobre"),
    path("carrinho", cart_list_view, name="cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)