from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
from views import *
from reinet import settings

urlpatterns = patterns('',

        url(r'^Demandas[/]?$',Demandas,name='Demandas'),
        url(r'^DemandaVer[/]?$',DemandaVer,name='DemandaVer'),
        url(r'^DemandaCrear[/]?$',DemandaCrear,name='DemandaCrear'),
        
              
        url(r'^Ofertas[/]?$',Ofertas,name='Ofertas'),
        url(r'^OfertaCrear[/]?$',OfertaCrear,name='OfertaCrear'),  
        url(r'^OfertaVer[/]?$',OfertaVer,name='OfertaVer'), 
        url(r'^OfertasMisOfertas[/]?$',OfertasMisOfertas,name='OfertasMisOfertas'), 
        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT})
        
)