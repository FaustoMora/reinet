from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *
urlpatterns = patterns('',

    url(r'^list-incubaciones/?$',ListIncubaciones.as_view(),name='list_incubaciones'),
    url(r'^incubacion[/]?$',homeIncubacion,name='home_incubacion'),
    url(r'^incubacion/crear[/]?$',crearIncubacion,name='crear_incubacion'),
    url(r'^incubacion/createInc[/]?$',createIncubacion,name='create_incubacion'),
    #url(r'^incubacion/(?P<identifier>\d+)$',incubacionDetails,name='detalle_incubacion'),
    url(r'^list-incubaciones/(?P<pk>\d+)$',IncDetails.as_view(),name='incubacion_detalle'),
    url(r'^list-incubadas/?$',IncubadasList.as_view(),name='lista_de_incubadas'),

)