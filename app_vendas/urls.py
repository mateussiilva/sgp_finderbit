from django.urls import path
from . import views

urlpatterns = [
    path("vendas",views.index,name="Pagina de vendas"),
    path("vendas/<int:pedido_id>",views.get_pedido,name="page_pedido")
]