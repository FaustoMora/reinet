from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *
from reinet import settings

urlpatterns = patterns('',

        url(r'^homeConcursos[/]?$',homeConcursos,name='homeConcursos'),
        url(r'^crearConcurso[/]?$',crearConcurso,name='crearConcurso'),
        url(r'^verConcurso[/]?$',verConcurso,name='verConcurso'),
        url(r'^editarConcurso[/]?$',editarConcurso,name='editarConcurso'),
        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
        url(r'^mostrarOfertas[/]$', mostrarOfertas, name="mostrarOfertas"),
		url(r'^registrarOferta[/]$', registrarOferta, name="registrarOfertas"),
		url(r'^searchConcursoRed[/]$', searchConcursoRed, name="registrarOfertas"),
		url(r'^gestionarInscripcion[/]$', gestionarInscripcion, name="gestionarInscripcion"),
		url(r'^milesperfil[/]$', milesperfil, name="milesperfil")

)