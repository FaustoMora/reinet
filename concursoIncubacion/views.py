# Create your views here.
from django.shortcuts import render_to_response, render
from django.core.files import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from forms import *
from models import *
from usuarios.models import *
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.context_processors import csrf

@login_required(login_url='/ingresar/')
def homeConcursos(request):
    lst_concursos = Concurso.objects.all().filter(idusuario=request.session['id_user'])[:8]
    return render_to_response('CONCURSO_inicio_concurso.html',{'lst_concursos' : lst_concursos},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearConcurso(request): 
	if request.POST: #POST
		form = CrearConcursoForm(request.POST, request.FILES)

		if form.is_valid():
			nuevoConcurso=super(CrearConcursoForm, form).save(commit=False)
			nuevoConcurso.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
			nuevoConcurso.estado=1
			nuevoConcurso.save()
			return HttpResponseRedirect('/homeConcursos')
		else:
			form = CrearConcursoForm()
	else:
		form=CrearConcursoForm()

	args={}
	args.update(csrf(request))
	args['form']=form
	return render_to_response('CONCURSO_crear_concurso.html', args)

@login_required(login_url='/ingresar/')
def verConcurso(request):
	idcon = int(request.GET.get('q', ''))
	concurso=Concurso.objects.get(idConcurso = idcon)
	args = {}
	args['concurso'] = concurso
	print concurso.descripcion
	return render_to_response('CONCURSO_perfil.html', args)

@login_required(login_url='/ingresar/')
def editarConcurso(request):
	idcon = int(request.GET.get('q', ''))
	print 'HERE HELLO!!!'
	print idcon
	if request.method == 'POST':
		concurso=Concurso.objects.get(idConcurso = idcon)
		form = CrearConcursoForm(request.POST, request.FILES, instance=concurso)
		if form.is_valid() :
			print 'Yeah'
			form.save()
			return HttpResponseRedirect('/homeConcursos')
		else:
			concursoForm = CrearConcursoForm(instance=concurso)
	else:
		print 'oh no'
		concurso=Concurso.objects.get(idConcurso = idcon)
		concursoForm = CrearConcursoForm(instance=concurso)
		
	args={}
	args.update(csrf(request))
	args['form']=concursoForm
	print concurso.nombre
	return render_to_response('CONCURSO_editar_concurso.html', args)

@login_required(login_url='/ingresar/')
def homeIncubacion(request):
	lst_incubacion = Incubacion.objects.all().filter(idusuario=request.session['id_user'])[:8]
	return render_to_response('INCUBACION_inicio.html',{'lst_incubacion' : lst_incubacion},context_instance=RequestContext(request))

    
@login_required(login_url='/ingresar/')
def verIncubacion(request):
	idincu = int(request.GET.get('q', ''))
	incubacion=Incubacion.objects.get(idIncubacion = idincu)
	args = {}
	args['incubacion'] = incubacion
	print incubacion.descripcion
	return render_to_response('INCUBACION_perfil.html',args)
    
@login_required(login_url='/ingresar/')    
def crearIncubacion(request):
	if request.POST: #POST
		form = CrearIncubacionForm(request.POST, request.FILES)

		if form.is_valid():
			nuevoIncubacion=super(CrearIncubacionForm, form).save(commit=False)
			nuevoIncubacion.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
			nuevoIncubacion.estado=1
			nuevoIncubacion.save()
			return HttpResponseRedirect('/homeIncubacion')
		else:
			form = CrearIncubacionForm()
	else:
		form=CrearIncubacionForm()

	args={}
	args.update(csrf(request))
	args['form']=form
	return render_to_response('INCUBACION_crear.html', args)


@login_required(login_url='/ingresar/')
def editarIncubacion(request):
	idincu = int(request.GET.get('q', ''))
	print 'HERE HELLO!!!'
	print idincu
	if request.method == 'POST':
		incubacion=Incubacion.objects.get(idIncubacion = idincu)
		form = CrearIncubacionForm(request.POST, request.FILES, instance=incubacion)
		if form.is_valid() :
			print 'Yeah'
			form.save()
			return HttpResponseRedirect('/homeIncubacion')
		else:
			incubacionForm = CrearIncubacionForm(instance=incubacion)
	else:
		print 'oh no'
		incubacion=Incubacion.objects.get(idIncubacion = idincu)
		incubacionForm = CrearIncubacionForm(instance=incubacion)
		
	args={}
	args.update(csrf(request))
	args['form']=incubacionForm
	print incubacion.nombre
	return render_to_response('INCUBACION_editar_incubacion.html', args)

