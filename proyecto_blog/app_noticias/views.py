from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# IMPORTANTE: Esta línea permite hacer búsquedas complejas (filtros)
from django.db import models 

# Importamos nuestros modelos y formularios
from .models import Noticias, Categorias
from .forms import ComentarioForm

# --- VISTAS BASADAS EN FUNCIONES (VBF) ---

def listar_noticias(request):
    # Empezamos con todas las noticias
    noticias = Noticias.objects.all()

    # Capturamos los datos del formulario de búsqueda (GET)
    busqueda = request.GET.get('buscar')
    categoria_id = request.GET.get('categoria')
    orden = request.GET.get('orden')

    # Filtro por texto (Título o Contenido) usando Q para buscar en ambos campos
    if busqueda:
        noticias = noticias.filter(
            models.Q(titulo__icontains=busqueda) | 
            models.Q(contenido__icontains=busqueda)
        )

    # Filtro por Categoría
    if categoria_id:
        noticias = noticias.filter(categoria_id=categoria_id)

    # Ordenar por fecha
    if orden == 'asc':
        noticias = noticias.order_by('fecha')
    else:
        noticias = noticias.order_by('-fecha')

    ctx = {
        'noticias': noticias,
        'categorias': Categorias.objects.all(),
        'titulo_pagina': "Explorar Noticias"
    }
    return render(request, "app_noticias/listar_noticias.html", ctx)

@login_required
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect("listar_noticias")
    return render(request, "categorias/eliminar_categoria.html")

@login_required
def agregar_comentario(request, pk):
    noticia = get_object_or_404(Noticias, pk=pk)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.noticia = noticia
            comentario.save()
            return redirect("detalle_noticia", pk=pk)
    return redirect("detalle_noticia", pk=pk)

# --- VISTAS BASADAS EN CLASES (VBC) ---

class NoticiasListView(ListView):
    model = Noticias
    template_name = "app_noticias/listar_noticias.html"
    context_object_name = "noticias"

@method_decorator(login_required, name='dispatch')
class NoticiaDetailView(DetailView):
    model = Noticias
    template_name = "app_noticias/detalle_noticia.html"
    context_object_name = "noticias"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioForm()
        return context

class NoticiaDeleteView(DeleteView):
    model = Noticias
    template_name = "app_noticias/eliminar_noticia.html"
    success_url = reverse_lazy("listar_noticias")