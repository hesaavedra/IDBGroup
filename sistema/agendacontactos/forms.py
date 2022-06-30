from dataclasses import fields
from pyexpat import model
from django import forms
from .models import contacto

class contactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields ='__all__'