from django.shortcuts import render

# Create your views here.

from .models import Sesion
from datetime import datetime
from django_ajax.decorators import ajax
from clase.models import Comentario
from django.template.loader import render_to_string

@ajax
def crear_comentario(request, pk):
    sesion = Sesion.objects.get(pk=pk)
    comentario = Comentario(
                            nombre=request.POST.get('inombre'),
                            texto=request.POST.get('icomentario')
                            )

    comentario.save()
    sesion.comentarios.add(comentario)
    return { 'inner-fragments': {
            '#myList_%d' % (sesion.pk,): render_to_string("comentarios.html", {'obj': sesion})
            },
        }



def vista(request):
    activas = Sesion.objects.filter(fecha_apertura__lte=datetime.now())
    return render(request, "index.html",
                    {'obj_list': activas})
