
from django.conf.urls.defaults import *
from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *

urlpatterns = patterns('',

    url(r'^index[/]?$',index,name='index'),
        url(r'^ingresar[/]?$',ingresar,name='index'),
)
