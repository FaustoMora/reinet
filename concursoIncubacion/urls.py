from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *

urlpatterns = patterns('',

		url(r'^homeConcursos[/]?$',homeConcursos,name='homeConcursos'),
        url(r'^crearConcurso[/]?$',crearConcurso,name='crearConcurso'),
        url(r'^verConcurso[/]?$',verConcurso,name='verConcurso')
		
)