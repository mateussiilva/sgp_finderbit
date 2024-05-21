from django.urls import path
from . import views

urlpatterns = [ 
    path("",views.index,name="Pagina Inicial"),
    # path("",views.index,name="Pagina Inicial"),
]