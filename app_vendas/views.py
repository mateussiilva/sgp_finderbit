from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    pedidos = models.Pedido.objects.all().values()
    context = {
        "pedidos": pedidos,
        "title_page": "Pagina de Vendas"
    }
    return render(request, "vendas/index.html", context=context)


def get_pedido(request, pedido_id):
    pedido = get_object_or_404(models.Pedido, id=pedido_id)
    print(pedido)
    context = {
        "pedido": pedido,
        # 'id':id,
        "title_page": "Pagina de pedidos"
    }
    return render(request, "vendas/pedidos.html", context=context)
