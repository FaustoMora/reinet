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
	tipo_user = request.session['tipo']
	if (tipo_user=="persona"):
		lst_concursos = Concurso.objects.all()[:8]
	elif (tipo_user=="institucion"):
		lst_concursos = Concurso.objects.all().filter(idusuario=request.session['id_user'])[:8]
	return render_to_response('CONCURSO_inicio_concurso.html',{'lst_concursos' : lst_concursos,'tipo_user':tipo_user},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearConcurso(request):
	if(request.session["tipo"]=="institucion"):
		if request.POST: #POST
			form = CrearConcursoForm(request.POST, request.FILES)

			if form.is_valid():

				val = validarfechas(form.cleaned_data['fecha_inicio'],form.cleaned_data['fecha_fin'])
				print val

				if val:
					nuevoConcurso=super(CrearConcursoForm, form).save(commit=False)
					nuevoConcurso.idusuario=Institucion.objects.get(idinstitucion=request.session['id_institucion'])
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
	else:
		return HttpResponseRedirect('/homeConcursos')

@login_required(login_url='/ingresar/')
def verConcurso(request):
	idcon = int(request.GET.get('q', ''))
	concurso=Concurso.objects.get(idConcurso = idcon)
	milestones = MilestoneConcurso.objects.all().filter(idConcurso = idcon)
	concursousuario=Concurso.objects.get(idConcurso = idcon).idusuario.id
	args = {}
	args['concurso'] = concurso

	if (concursousuario == request.session['id_user']):
		val = True;
	else:
		val = False;
	print "Probado"
	print concursousuario
	print request.session['id_user']
	print val
	args['val'] = val
	args['milestones'] = milestones
	args['nums'] = range(len(milestones))
	return render_to_response('CONCURSO_perfil.html', args)

@login_required(login_url='/ingresar/')
def editarConcurso(request):
	if(request.session["tipo"]=="institucion"):
		idcon = int(request.GET.get('q', ''))
		print 'HERE HELLO!!!'
		print idcon
		if request.method == 'POST':
			concurso=Concurso.objects.get(idConcurso = idcon)
			form = EditarConcursoForm(request.POST, request.FILES, instance=concurso)
			if form.is_valid() :
				print 'Yeah'
				form.save()
				return HttpResponseRedirect('/homeConcursos')
			else:
				concursoForm = EditarConcursoForm(instance=concurso)
		else:
			print 'oh no'
			concurso=Concurso.objects.get(idConcurso = idcon)
			print "debug"
			print concurso.idusuario
			print request.session['id_user']
			if (concurso.idusuario.id != request.session['id_user']):
				return HttpResponseRedirect('/homeConcursos')
			concursoForm = EditarConcursoForm(instance=concurso)
			
		args={}
		args.update(csrf(request))
		args['form']=concursoForm
		print concurso.nombre
		return render_to_response('CONCURSO_editar_concurso.html', args)
	else:
		return HttpResponseRedirect('/homeConcursos')


def validarfechas(fechaIn, fechaOut):
	if fechaIn:
		if fechaOut:
			if fechaIn < fechaOut:
				return True
	return False

def compararIds(idA, idB):
	print idA
	print idB
	if idA is idB:
		return True
	return False



