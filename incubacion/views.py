from django.core.exceptions import FieldError
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, Http404,HttpResponseNotFound
from django.contrib.auth import decorators
from ofertaDemanda.models import Oferta
from usuarios.models import Institucion, Persona
from incubacion.models import Incubacion, Incubada
from restless.modelviews import Endpoint
from restless.auth import BasicHttpAuthMixin,login_required
from restless.models import serialize


# Create your views here.



class ListIncubaciones(Endpoint, BasicHttpAuthMixin):
    @login_required
    def get(self, request):
        incs=[]
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
            ('estado',dict(
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
            ))])


@decorators.login_required(login_url='/ingresar/')
def homeIncubacion(request):
    return render(request,'incubacion_main.html')