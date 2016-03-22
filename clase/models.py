from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
# Create your models here.


@python_2_unicode_compatible
class Comentario(models.Model):
    nombre = models.CharField(max_length=150, null=True)
    texto = models.CharField(max_length=1030)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True)

    def __str__(self):
        return "%s -- %s" % (str(self.fecha), self.nombre or "Anonymus")


@python_2_unicode_compatible
class Sesion(models.Model):
    fecha_apertura = models.DateTimeField()
    archivo = models.FileField(upload_to="files/%Y")
    sistematizacion = models.FileField(
        upload_to="sistematizacion/%Y", null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    comentarios = models.ManyToManyField(Comentario, blank=True)

    def __str__(self):
        return self.titulo
