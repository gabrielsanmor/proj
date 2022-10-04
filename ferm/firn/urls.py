from re import template
from django.urls import path
from firn import views
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

urlpatterns = [
    path("", home_list_view, name="home"),
    path("<str:result>", home_list_view, name="home"),
    path("loja", views.loja, name="loja"),
    path("sobre", views.sobre, name="sobre"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)