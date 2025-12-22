from django.contrib import admin
from .models import Noticias, Categorias, Comentario

# Registro básico de Categorías
admin.site.register(Categorias)

# Configuración personalizada para Noticias
@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'fecha')
    list_filter = ('categoria', 'autor', 'fecha')
    search_fields = ('titulo', 'contenido')

# Configuración para Comentarios
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('autor', 'noticia', 'fecha')
    list_filter = ('fecha', 'autor')
    search_fields = ('cuerpo',)