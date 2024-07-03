from django.urls import path

from .views import index

urlpatterns = [
    path("clientes",index,name="page_clients")
]