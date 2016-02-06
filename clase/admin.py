from django.contrib import admin

# Register your models here.
from .models import Comentario, Sesion

admin.site.register([Comentario, Sesion])