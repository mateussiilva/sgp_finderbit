from django.shortcuts import render

# Create your views here.
# from
from .models import Cliente

def index(request):
    clientes = Cliente.objects.all().values()
    print(clientes)
    context = {
        "clientes": clientes
    }
    return render(request,template_name="clientes/index.html",context=context)