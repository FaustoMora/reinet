from django.core.exceptions import FieldError
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, Http404,HttpResponseNotFound,HttpResponseRedirect
from django.contrib.auth import decorators
from django.utils.dateparse import parse_date
from app.models import Catalogo
from ofertaDemanda.models import Oferta
from usuarios.models import Institucion, Persona
from incubacion.models import Incubacion, Incubada, TiposOfertasIncubacion
from restless.modelviews import Endpoint,ListEndpoint, DetailEndpoint
from restless.auth import BasicHttpAuthMixin,login_required
from restless.models import serialize
from django.views.decorators.csrf import csrf_exempt


# Create your views here.



class ListIncubaciones(ListEndpoint, BasicHttpAuthMixin):
    model = Incubacion
    @login_required
    def get(self, request):
        incs = []
        try:
            temp = request.session['id_institucion']
            inst = Institucion.objects.get(idinstitucion=temp)
            incs = Incubacion.objects.filter(autor=inst)
        except KeyError:
            temp = request.user
            temp = Oferta.objects.filter(idusuario=temp)
            for of in temp:
                incubada = Incubada.objects.get(oferta=of)
                incs.append(incubada.incubacion)
        return serialize(incs, include=[
            ('alcance', dict(
                fields=[
                    'codigo',
                    'descripcion',
                    ]
            )),
            ('autor',dict(
                fields=[
                    'nombre_corto'
                ]
            )),
            ('tipoOfertas',dict(
                fields=[
                    'codigo',
                    'descripcion',
                ]
            )),
            ('ofertasIncubadas',
             lambda a: a.countIncubadas()
            )
        ])


@decorators.login_required(login_url='/ingresar/')
def homeIncubacion(request):
    #return render(request, 'incubacion_main.html')
    return render(request, 'index-incubacion.html')



@decorators.login_required(login_url='/ingresar/')
def crearIncubacion(request):
    return render(request, 'crear_incubacion.html')

@csrf_exempt
@decorators.login_required(login_url='/ingresar/')
def createIncubacion(request):
    i = Incubacion()
    i.nombre = request.POST.get('nombre')
    i.descripcion = request.POST.get('descripcion')
    i.condiciones = request.POST.get('condiciones')
    i.perfiles = request.POST.get('perfiles')
    #i.alcance = Catalogo.objects.get(request.POST.get("alcanc"))
    i.alcance = Catalogo.objects.get(id=2)
    temp = request.POST.getlist('tipoOf')
    autor = Institucion.objects.get(idinstitucion=request.session['id_institucion'])
    i.autor = autor
    i.estado = Catalogo.objects.get(id=8)
    i.save()

    for a in temp:
        y = TiposOfertasIncubacion()
        y.incubacion=i
        y.tipo = Catalogo.objects.get(id=int(a))
        y.save()
    return HttpResponseRedirect('/incubacion')

@decorators.login_required(login_url='/ingresar/')
def incubacionDetails(request,identifier):
    i = Incubacion.objects.get(id=int(identifier))
    context = {"incubacion":i,}

    return render(request,"incubacion_institucion.html",context)


class IncDetails(DetailEndpoint):
    model = Incubacion


class IncubadasList(ListEndpoint):
    model = Incubada