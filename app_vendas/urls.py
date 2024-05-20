from django.urls import path
from . import views

urlpatterns = [
    path("vendas",views.index,name="Pagina de vendas")
]