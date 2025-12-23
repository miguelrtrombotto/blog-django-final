from django.urls import path
from . import views
from .views import NoticiasListView, NoticiaDetailView, NoticiaDeleteView

urlpatterns = [
    # Rutas para Noticias
    path("noticias/", views.listar_noticias, name="listar_noticias"),
    path("detalle_noticia/<int:pk>/", NoticiaDetailView.as_view(), name="detalle_noticia"),
    path("eliminar_noticia/<int:pk>/", NoticiaDeleteView.as_view(), name="eliminar_noticia"),

    # Rutas para Categorías
    path("eliminar_categoria/<int:pk>/", views.eliminar_categoria, name="eliminar_categoria"),

    # Ruta para Comentarios (NUEVA)
    path("agregar_comentario/<int:pk>/", views.agregar_comentario, name="agregar_comentario"),
]