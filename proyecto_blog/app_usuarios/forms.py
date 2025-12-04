from django.contrib.auth.forms import UserCreationForm

# modelo por defecto de usuarios django
from django.contrib.auth.models import User
from django import forms


class PersonalizadoUserCreationForm(UserCreationForm):

    email = forms.EmailField(required=True, help_text="Campo obligatorio")

    class Meta:
        model = User
        fields = ("username", "email")