from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *
from reinet import settings

urlpatterns = patterns('',

        url(r'^homeDemandas[/]?$',homeDemandas,name='homeDemandas'),
        url(r'^verDemanda[/]?$',verDemanda,name='verDemanda'),
        url(r'^crearDemanda[/]?$',crearDemanda,name='crearDemanda'),    
        url(r'^misDemandas[/]?$',misDemandas,name='misDemandas'),            
        url(r'^homeOfertas[/]?$',homeOfertas,name='homeOfertas'),
        url(r'^crearOferta[/]?$',crearOferta,name='crearOferta'),  
        url(r'^matricular/(?P<idalumno>\d+)/(?P<idcurso>\d+)/$',
      'make_matricula',
      name='modulo-matriculas-add'),

        
        url(r'^verOferta[/]?$',verOferta,name='verOferta'),
        url(r'^editarOferta[/]?$',editarOferta,name='editarOferta'),   
        url(r'^misOfertas[/]?$',misOfertas,name='misOfertas'), 



        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT})
        
)
