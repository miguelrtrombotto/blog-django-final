
from django.urls import path
from . import views
from .views import NoticiasListView, NoticiaDetailView, NoticiaDeleteView

urlpatterns = [
    # url para vista en funciones
    path("noticias/", views.listar_noticias, name="listar_noticias"),

    # url para vista en clases
    # path("noticias2/", NoticiasListView.as_view(), name="listar_noticias"),
    path("detalle_noticia/<int:pk>", NoticiaDetailView.as_view(), name="detalle_noticia"),
    path("eliminar_noticia/<int:pk>", NoticiaDeleteView.as_view()),

    # url categoria funcion
    path("eliminar_categoria/<int:pk>", views.eliminar_categoria)
]