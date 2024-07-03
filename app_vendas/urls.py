from django.urls import path
from . import views

urlpatterns = [
    path("vendas",views.index,name="app_vendas"),
    # path("vendas/<int:pedido_id>",views.get_pedido,name="page_pedido")
]