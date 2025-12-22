from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['cuerpo']
        widgets = {
            'cuerpo': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu comentario aquí...',
                'rows': 3
            }),
        }
        labels = {
            'cuerpo': '',
        }