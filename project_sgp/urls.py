from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("",include("home_page.urls")),
    path("",include("app_vendas.urls")),
    path("admin/", admin.site.urls),
]
