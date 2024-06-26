from django.shortcuts import render,get_object_or_404
from . import models
# from 
# Create your views here.

def index(request):
    pedidos = models.Pedido.objects.all().values()
    context = {
        "pedidos":pedidos,
        "title_page":"Pagina de Vendas"
    }
    return render(request,"index_vendas.html", context=context)

def get_pedido(request,pedido_id):
    pedido = get_object_or_404(models.Pedido, id=pedido_id)
    print(pedido)
    context = {
        "pedido":pedido,
        # 'id':id,
        "title_page":"Pagina de pedidos"
    }
    return render(request,"pedidos.html", context=context)
