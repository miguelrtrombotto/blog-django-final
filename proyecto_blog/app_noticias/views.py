from django.shortcuts import render
from .models import Noticias, Categorias
from django.contrib.auth.models import User

# Create your views here.

# from .models import Noticias
# Noticias.objects.all() === SELECT * FROM noticias;
# Objeto.delete() === DELETE FROM noticias WHERE id=4;

# funciones (VBF)
def listar_noticias(request):
    noticias = Noticias.objects.all()

    ctx = {
        'noticias': noticias,
        'titulo_pagina': "Ultimas noticias"
    }

    return render(request, "app_noticias/listar_noticias.html", ctx)

# clases (VBC) genericas
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
class NoticiasListView(ListView):
    model = Noticias
    template_name = "app_noticias/listar_noticias.html"
    context_object_name = "noticias"

class NoticiaDetailView(DetailView):
    model = Noticias
    template_name = "app_noticias/detalle_noticia.html"

class NoticiaDeleteView(DeleteView):
    model = Noticias
    template_name = "app_noticias/eliminar_noticia.html"
    success_url = reverse_lazy("listar_noticias")



# eliminar categoria VBF

from django.shortcuts import get_object_or_404, redirect

def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categorias, pk=pk)

    if request.method == "POST":
        categoria.delete()
        return redirect("listar_noticias")
    
    return render(request, "categorias/eliminar_categoria.html")