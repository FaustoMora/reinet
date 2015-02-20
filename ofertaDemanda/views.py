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
def Demandas(request):
    return render_to_response('DEMANDA_Inicio.html')

@login_required(login_url='/ingresar/') 
def DemandaCrear(request):
    return render_to_response('DEMANDA_crear_demanda.html')

@login_required(login_url='/ingresar/') 
def DemandaVer(request):
    return render_to_response('DEMANDA_perfil.html')

@login_required(login_url='/ingresar/') 
def Ofertas(request):
	lst_ofertas = Oferta.objects.all()[:4]
	return render_to_response('OFERTA_Inicio2.html', {'lst_ofertas' : lst_ofertas}, context_instance=RequestContext(request))






@login_required(login_url='/ingresar/')
def OfertaCrear(request):
	if request.POST: #POST
		form = CrearOfertaForm(request.POST, request.FILES)

		if form.is_valid():
			nuevaOferta=super(CrearOfertaForm, form).save(commit=False)
			nuevaOferta.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
			nuevaOferta.estado=1
			nuevaOferta.save()
			return HttpResponseRedirect('/Ofertas')
		else:
			form = CrearOfertaForm()
	else:
		form=CrearOfertaForm()

	args={}
	args.update(csrf(request))
	args['form']=form
	return render_to_response('OFERTA_crear_oferta.html')
	
@login_required(login_url='/ingresar/') 
def OfertaVer(request):
    return render_to_response('OFERTA_perfil.html')

@login_required(login_url='/ingresar/') 
def OfertasMisOfertas(request):
	lst_ofertas = Oferta.objects.all()[:4]
	return render_to_response('OFERTA_misOfertas.html', {'lst_ofertas' : lst_ofertas}, context_instance=RequestContext(request)) 