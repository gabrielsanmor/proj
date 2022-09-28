from django.urls import path
from firn import views

urlpatterns = [
    path("", views.home, name="home"),
    path("loja", views.loja, name="loja"),
    path("sobre", views.sobre, name="sobre"),
]