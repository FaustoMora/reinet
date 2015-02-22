from django.shortcuts import render_to_response, render
from django.core.files import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from usuarios.models import *
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.context_processors import csrf
from forms import *

@login_required(login_url='/ingresar/') 
def homeDemandas(request):
    return render_to_response('DEMANDA_Inicio.html')

@login_required(login_url='/ingresar/') 
def crearDemanda(request):
    return render_to_response('DEMANDA_crear_demanda.html')

@login_required(login_url='/ingresar/') 
def verDemanda(request):
    return render_to_response('DEMANDA_perfil.html')

@login_required(login_url='/ingresar/') 
def misDemandas(request):
    return render_to_response('DEMANDA_Inicio.html')    

@login_required(login_url='/ingresar/') 
def homeOfertas(request):
	lst_ofertas = Oferta.objects.all()[:4]
	return render_to_response('OFERTA_Inicio2.html', {'lst_ofertas' : lst_ofertas}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearOferta(request):
    form = CrearOfertaForm(request.POST, request.FILES)

    if form.is_valid():
        nuevaOferta=super(CrearOfertaForm, form).save(commit=False)
        nuevaOferta.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
        nuevaOferta.estadoOferta=1
        nuevaOferta.ofertaPublicada = 1            
        nuevaOferta.save()
        return HttpResponseRedirect('misOfertas')

    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('OFERTA_crear_oferta.html',args)


	
@login_required(login_url='/ingresar/') 
def verOferta(request):
    return render_to_response('OFERTA_perfil.html')


@login_required(login_url='/ingresar/') 
def editarOferta(request):    
    return render_to_response('OFERTA_perfil.html')


@login_required(login_url='/ingresar/') 
def misOfertas(request):
	lst_ofertas = Oferta.objects.all()[:4]
	return render_to_response('OFERTA_misOfertas.html', {'lst_ofertas' : lst_ofertas}, context_instance=RequestContext(request)) 