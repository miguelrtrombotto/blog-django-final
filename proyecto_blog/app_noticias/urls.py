
from django.urls import path
from . import views

urlpatterns = [
    path("noticias/", views.listar_noticias, name="listar_noticias")
]