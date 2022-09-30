from re import template
from django.urls import path
from firn import views
from .models import Item
from django.conf import settings
from django.conf.urls.static import static

home_list_view= views.HomeListView.as_view(
    queryset=Item.objects.filter(categoria__nome="Higiene Pessoal")[:5],
    context_object_name="itensHP",
    template_name="firn/home.html"
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("loja", views.loja, name="loja"),
    path("sobre", views.sobre, name="sobre"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)