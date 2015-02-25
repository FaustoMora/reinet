from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import ListIncubaciones,homeIncubacion,crearIncubacion, createIncubacion,incubacionDetails
urlpatterns = patterns('',

    url(r'^list-incubaciones[/]?$',ListIncubaciones.as_view(),name='list_incubaciones'),
    url(r'^incubacion[/]?$',homeIncubacion,name='home_incubacion'),
    url(r'^incubacion/crear[/]?$',crearIncubacion,name='crear_incubacion'),
    url(r'^incubacion/createInc[/]?$',createIncubacion,name='create_incubacion'),
    url(r'^incubacion/(?P<identifier>\d+)$',incubacionDetails,name='create_incubacion'),


)