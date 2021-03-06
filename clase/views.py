from django.shortcuts import render

# Create your views here.

from .models import Sesion
from datetime import datetime
from django_ajax.decorators import ajax
from clase.models import Comentario
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


@ajax
def crear_comentario(request, pk):
    sesion = Sesion.objects.get(pk=pk)
    comentario = Comentario(
        nombre="no se usa mas",
        texto=request.POST.get('icomentario')
    )
    comentario.usuario = request.user
    comentario.save()
    sesion.comentarios.add(comentario)
    return {'inner-fragments': {
        '#myList_%d' % (sesion.pk,): render_to_string("comentarios.html",
                                                      {'obj': sesion,
                                                       'pk': pk,
                                                       'limpia': True
                                                       })
    },
    }


@login_required
def vista(request):
    activas = Sesion.objects.filter(fecha_apertura__lte=datetime.now())
    return render(request, "index.html",
                  {'obj_list': activas})
