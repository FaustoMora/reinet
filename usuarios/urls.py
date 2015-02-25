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


        url(r'^registerInst[/]?$',registerInst,name='index'),
        url(r'^perfilInst[/]?$',perfil_institucion),
        url(r'^editarperfilInst[/]?$',editar_perfil_institucion),
        url(r'^inicio_view[/]?$',verInicioF,name='index'),
        url(r'^$',index,name='index'),
        url(r'^perfil[/]?$',perfil_view),    
        url(r'^mensajes[/]?$',mensajes_view),   
        url(r'^enviarmensaje[/]?$',enviar_mensaje),   
        url(r'^busqueda[/]?$',busqueda_view),
        url(r'^editarperfil[/]?$',editar_perfil_view),
        url(r'^actualizarFoto[/]?$',subir_imagen),
        url(r'^mensajesEnviados[/]?$',mensajesEnviados_view),
        url(r'^verPerfil[/]?$',verPerfil),    
        url(r'^verMensaje[/]?$',verMensaje),   
        url(r'^busquedaOferta[/]?$',busqueda_oferta),
        url(r'^busquedaDemanda[/]?$',busqueda_demanda),
        url(r'^busquedaConcurso[/]?$',busqueda_concursos),
        url(r'^busquedaUsuario[/]?$',busqueda_usuario), 
        url(r'^terminosCondiciones[/]?$',terminos), 
  
)
