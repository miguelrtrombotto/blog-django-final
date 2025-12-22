from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías"

class Noticias(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noticias")
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True, blank=True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    # Cambiamos None por 'noticias' para que las fotos se guarden bien
    imagen = models.ImageField(upload_to='noticias', null=True, blank=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Noticias"
        # Orden predeterminado por fecha descendente (más nuevas primero)
        ordering = ['-fecha']

# REQUISITO: Sistema de Comentarios
class Comentario(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    cuerpo = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.noticia}"