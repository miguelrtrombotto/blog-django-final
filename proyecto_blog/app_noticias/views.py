from django.shortcuts import render
from .models import Noticias, Categorias
from django.contrib.auth.models import User

# Create your views here.

# from .models import Noticias
# Noticias.objects.all() === SELECT * FROM noticias;
# Objeto.delete() === DELETE FROM noticias WHERE id=4;

# funciones
def listar_noticias(request):
    noticias = Noticias.objects.all()

    ctx = {
        'noticias': noticias,
        'titulo_pagina': "Ultimas noticias"
    }

    return render(request, "app_noticias/listar_noticias.html", ctx)

# clases