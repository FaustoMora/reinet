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
    tipo_user = 'institucion'#request.session['tipo']
    return render_to_response('CONCURSO_inicio_concurso.html',{'lst_concursos' : lst_concursos,'tipo_user':tipo_user},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearConcurso(request): 
	if request.POST: #POST
		form = CrearConcursoForm(request.POST, request.FILES)

		val = validarfechas(form.fecha_inicio,form.fecha_fin)
		print val 

		if form.is_valid() and val:
			nuevoConcurso=super(CrearConcursoForm, form).save(commit=False)
			nuevoConcurso.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
			nuevoConcurso.estado=1
			nuevoConcurso.ranking=0
			nuevoConcurso.save()
			
			lenl = 0;
			lenl = len(request.POST.getlist("mileReq"))
			
			print lenl
			for i in range(0, lenl):
				mile = MilestoneConcurso()
				mile.fecha_entrega= request.POST.getlist("mileFecha")[i]
				mile.peso = request.POST.getlist("milePeso")[i]
				mile.requerimiento = request.POST.getlist("mileReq")[i]
				mile.estado = 1;
				mile.idConcurso = nuevoConcurso;
				mile.save()
			
			info="Concurso creado correctamente"
			return HttpResponseRedirect('/homeConcursos')
		else:
			info="Error Datos incorrectos"

		form = CrearConcursoForm()
		messages.success(request, info)
		return HttpResponseRedirect('/crearConcurso')
	else:
		form=CrearConcursoForm()

	args={}
	args.update(csrf(request))
	args['form']=form
	return render_to_response('CONCURSO_crear_concurso.html', args,context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def verConcurso(request):
	idcon = int(request.GET.get('q', ''))
	concurso=Concurso.objects.get(idConcurso = idcon)
	args = {}
	args['concurso'] = concurso

	"""
	if request.session['tipo'] == 'institucion':
		args['sessionid'] = Institucion.objects.get(idinstitucion=request.session['id_institucion'])
	elif request.session['tipo'] == 'persona':
		args['sessionid'] = Persona.objects.get(idpersona=request.session['id_persona'])"""

	args['sessionid'] = Persona.objects.get(idpersona=request.session['id_persona'])	

	val = compararIds(concurso.idusuario,args['sessionid'])
	print val
	args['val']=val
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


def validarfechas(fechaIn, fechaOut):
	if fechaIn < fechaOut:
		return True
	return False

def compararIds(idA, idB):
	if idA == idB:
		return True
	return False


""" VIEWS DE INCUBACION --- DEBEN MUDARSE """


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

