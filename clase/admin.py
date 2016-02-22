from django.contrib import admin

# Register your models here.
from .models import Comentario, Sesion

from django import forms
from redactor.widgets import RedactorEditor


class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        widgets = {
           'descripcion': RedactorEditor(),
        }
        fields = '__all__'

class SesionAdim(admin.ModelAdmin):
    form = SesionForm

admin.site.register(Sesion, SesionAdim)
admin.site.register(Comentario)
