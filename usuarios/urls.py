from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *

urlpatterns = patterns('',

		url(r'^index[/]?$',index,name='index'),
        url(r'^ingresar[/]?$',ingresar,name='index'),
        url(r'^logout[/]?$',logout,name='index'),
        url(r'^auth[/]?$',auth_view,name='index'),
        url(r'^loggedin[/]?$',loggedin,name='index'),
        url(r'^invalid[/]?$',invalid,name='index'),
        url(r'^register[/]?$',register,name='index'),
        url(r'^register_success[/]?$',register_success,name='index'),
        url(r'^create[/]?$',create,name='index'),
        url(r'^$',index,name='index'),
        url(r'^perfil[/]?$',perfil_view,name='index'),    
       
)
