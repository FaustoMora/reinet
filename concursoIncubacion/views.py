# Create your views here.
from django.shortcuts import render_to_response, render
from django.core.files import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from forms import *
from models import *
from ofertaDemanda.models import *
from usuarios.models import *
from usuarios.views import *
from usuarios.urls import *
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.context_processors import csrf
from datetime import datetime
from datetime import date


#funciones de crear,ver,editar

@login_required(login_url='/ingresar/')
def homeConcursos(request):
	try:
		tipo_user = request.session['tipo']
		if (tipo_user=="persona"):
			lst_concursos = Concurso.objects.all()[:8]
		elif (tipo_user=="institucion"):
			lst_concursos = Concurso.objects.all().filter(idusuario=request.session['id_user'])[:8]
		return render_to_response('CONCURSO_inicio_concurso.html',{'lst_concursos' : lst_concursos,'tipo_user':tipo_user},context_instance=RequestContext(request))
	except:
		return HttpResponseRedirect('/RNNotFound')


@login_required(login_url='/ingresar/')
def crearConcurso(request):
	try:
		if(request.session["tipo"]=="institucion"):
			if request.POST: #POST
				form = CrearConcursoForm(request.POST, request.FILES)
				print "hace post"
				if form.is_valid():

					#####  validaciones de fechas
					val1 = validarfechas(form.cleaned_data['fecha_inicio'],form.cleaned_data['fecha_fin'])
					print val1

					val2 = False
					val3 = False
					val5 = False
					lenl = 0;
					lenl = len(request.POST.getlist("mileReq"))

					for i in range(0, lenl):
						print "Primer FOR"
						formato='%Y-%m-%d'
						aux = datetime.strptime(request.POST.getlist("mileFecha")[i], formato).date()
						#print aux 
						val2 = validarfechas(form.cleaned_data['fecha_inicio'],aux)
						#print val2
						val3 = validarfechas(aux,form.cleaned_data['fecha_fin'])
						#print val3
						if val2 == False:
							break
						if val3 == False:
							break
					####################################

					#####   validaciones de numeros negativos
					val4 = mayorCero(request.POST.getlist("milePeso")[i]) and mayorCero(form.cleaned_data['num_finalistas'])
					#print val4
					##################################


					##  validaciones de jurado #######
					len2=0
					len2= len(request.POST.getlist("jurado"))
					print "val Jurado"
					for i in range(0, len2):
						user_jurado_name = request.POST.getlist("jurado")[i]
						user_jurado = User.objects.get(username=user_jurado_name)

						try:
							aux_jurado = Institucion.objects.get(user_ptr_id=user_jurado.id)
							val6=False
						except:
							val6=True

						if val6:
							if user_jurado:
								val5=True
							else:
								val5=False
								break
						else:
							val5=False
							break

					print val5

					######################################

					if val1 and val2 and val3 and val4  and val5:
						print "pasa prueba"
						nuevoConcurso=super(CrearConcursoForm, form).save(commit=False)
						nuevoConcurso.idusuario=Institucion.objects.get(idinstitucion=request.session['id_institucion'])
						nuevoConcurso.estado=1
						nuevoConcurso.ranking=0
						nuevoConcurso.save()

						#for para ingresar jurado
						for i in range(0, len2):
							user_jurado_name = request.POST.getlist("jurado")[i]
							user_jurado = User.objects.get(username=user_jurado_name)
							jurado = Jurado()
							jurado.idusuario = user_jurado
							jurado.idConcurso = nuevoConcurso
							jurado.save()

						#for para ingresar milestone
						for i in range(0, lenl):
							mile = MilestoneConcurso()
							mile.fecha_entrega= request.POST.getlist("mileFecha")[i]
							mile.peso = request.POST.getlist("milePeso")[i]
							mile.requerimiento = request.POST.getlist("mileReq")[i]
							mile.estado = 1
							mile.idConcurso = nuevoConcurso
							mile.save()

						print "crea"
						info="Concurso creado correctamente"
						return HttpResponseRedirect('/homeConcursos')

					else:
						info="Error Datos incorrectos"
				else:
					print"no form"
					info="Error Datos incorrectos"

				form = CrearConcursoForm()
				messages.success(request, info)
				return HttpResponseRedirect('/crearConcurso')
				
			else: #GET
				form=CrearConcursoForm()

			args={}
			args.update(csrf(request))
			args['form']=form
			return render_to_response('CONCURSO_crear_concurso.html', args,context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/crearConcurso')
	except:
		args={}
		info="Error Datos incorrectos"
		args['form']=form
		messages.success(request,info)
		return HttpResponseRedirect('/crearConcurso')


@login_required(login_url='/ingresar/')
def verConcurso(request):
	try:
		idcon = int(request.GET.get('q', ''))
		concurso=Concurso.objects.get(idConcurso = idcon)
		milestones = MilestoneConcurso.objects.filter(idConcurso = idcon)
		concursousuario=Concurso.objects.get(idConcurso = idcon).idusuario.id
		args = {}
		args.update(csrf(request))
		args['concurso'] = concurso

		val = compararIds(concursousuario,request.session['id_user'])
		
		if (request.session["tipo"] == 'persona'):
			val2 = True;
		else:
			val2 = False;
			if (val == False):
				return HttpResponseRedirect('/homeConcursos')
		try:
			inscrip = Inscripcion.objects.all().filter(idConcurso = idcon, estado = 0)
			print len(inscrip)
		except:
			print "no hay inscripcion"
			inscrip = ""
			
		try:
			siInscrip = Inscripcion.objects.all().filter(idConcurso = idcon, estado = 1)
			print len(siInscrip)
		except: 
			print "no hay inscripciones aceptadas"
			siInscrip = ""
		print "Probado"
		print concursousuario
		print request.session['id_user']
		print val


		ofertas = Oferta.objects.filter(idusuario=request.session['id_user'])
		valinsc=False
		for o in ofertas:
			try:
				ins = Inscripcion.objects.get(idConcurso = idcon, idOferta = o.idOferta)
				print "op"
				valinsc = True
			except:
				valinsc = False
		print valinsc
		
		args['val'] = val
		args['val2'] = val2
		args['valinsc']=valinsc
		args['timenow'] = date.today()
		args['milestones'] = milestones
		args['nums'] = range(len(milestones))
		args['inscrip'] = inscrip
		args['participantes'] = siInscrip
		return render_to_response('CONCURSO_perfil.html', args)
	except:
		return HttpResponseRedirect('/RNNotFound')



@login_required(login_url='/ingresar/')
def editarConcurso(request):
	try:
		if(request.session["tipo"]=="institucion"):
			info=""
			idcon = int(request.GET.get('q', ''))
			print 'HERE HELLO!!!'
			print idcon
			if request.method == 'POST':
				concurso=Concurso.objects.get(idConcurso = idcon)
				fechafin = concurso.fecha_fin
				form = EditarConcursoForm(request.POST, request.FILES, instance=concurso)
				if form.is_valid() :

					print fechafin
					print form.cleaned_data['fecha_fin']

					if validarfechas(fechafin,form.cleaned_data['fecha_fin']):
						print 'Yeah'
						form.save()
						return HttpResponseRedirect('/homeConcursos')
					else:
						info="Error en la fecha final, la nueva fecha final no puede ser menor a la ya existente"
						concursoForm = EditarConcursoForm(instance=concurso)
				else:
					concursoForm = EditarConcursoForm(instance=concurso)
			else:
				print 'oh no'
				concurso=Concurso.objects.get(idConcurso = idcon)
				print concurso.idusuario
				print request.session['id_user']
				if not compararIds(concurso.idusuario.id,request.session['id_user']):
					return HttpResponseRedirect('/homeConcursos')
				concursoForm = EditarConcursoForm(instance=concurso)
				
			args={}
			args.update(csrf(request))
			args['form']=concursoForm
			args['idconcu'] = idcon
			print concurso.nombre
			messages.success(request, info)
			return render_to_response('CONCURSO_editar_concurso.html', args,context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/homeConcursos')
	except:
			return HttpResponseRedirect('/RNNotFound')



#funciones para validaciones

def validarfechas(fechaIn, fechaOut):
	if fechaIn:
		if fechaOut:
			if fechaIn < fechaOut:
				return True
	return False

def compararIds(idA, idB):
	print idA
	print idB
	if idA == idB:
		return True
	return False


def mayorCero(a):
	if a < 0:
		return False
	return True


def fechasiguales(fechaIn,fechaOut):
	if fechaIn:
		if fechaOut:
			if fechaIn == fechaOut:
				return True
	return False	


#funciones para ajax

def mostrarOfertas(request):
	print "requested!!!"
	ofert = Oferta.objects.all().filter(idusuario=request.session['id_user'])
	args = {}
	args['ofertas'] = ofert
	return render_to_response('ajax_busqueda_ofertas.html', args)
		
def registrarOferta(request):
	i = 0
	val = False;
	print 'registro!!'
	indice = request.POST['indice']
	concu = request.POST['concu']
	inscri = Inscripcion()
	ofertas = Oferta.objects.all().filter(idusuario=request.session['id_user'])
	for o in ofertas:
		if(i == int(indice)):
			print 'YEAH'
			inscri.idOferta = o
			print concu
			print o.idOferta
			try:
				ins = Inscripcion.objects.get(idConcurso = concu, idOferta = o.idOferta)
				print "op"
				val = False
			except:
				val = True
		i = i+1
	inscri.idConcurso = Concurso.objects.get(idConcurso = concu)
	inscri.estado = 0
	inscri.fecha = datetime.now().strftime('%Y-%m-%d')
	print val
	args = {}
	if (val):
		inscri.save()
		args['msj'] = "Oferta Inscrita Exitosamente!"
	else:
		args['msj'] = "La Oferta ya fue Inscrita Anteriormente"
	return render_to_response('ajax_vaciar.html', args)

def gestionarInscripcion(request):
	idInscrip = request.POST['idinscrip']
	valor = request.POST['value']
	print idInscrip
	inscrip = Inscripcion.objects.get(idInscripcion = idInscrip)
	inscrip.estado = valor
	inscrip.save()
	return render_to_response('empty.html');


def searchConcursoRed(request):
    errors= []
    if 'busquedaOfertaRed' in request.GET:
        busquedaOfertaRed = request.GET['busquedaOfertaRed']
        if not busquedaOfertaRed:
            errors.append('Ingrese un termino a buscar')
        elif len(busquedaOfertaRed)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            ofertas = Concurso.objects.filter(nombre__icontains=busquedaOfertaRed).exclude(idusuario = request.session['id_user'])
            return render(request, 'CONCURSO_inicio_concurso.html',
                {'ofertas':ofertas,'nombre':busquedaOfertaRed,'buscarOfer':True})
        return render(request,'CONCURSO_inicio_concurso.html',{'errors':errors})  


def milesperfil(request):
	print "estoy aca"
	miles_id = request.POST.get('idmiles')
	print miles_id

	if miles_id: 
		milestone = MilestoneConcurso.objects.get(idMilestone = miles_id)
		print milestone
		print milestone.idConcurso.idConcurso
		concurso = Concurso.objects.get(idConcurso = milestone.idConcurso.idConcurso)
		jurado_lst = Jurado.objects.filter(idConcurso = milestone.idConcurso.idConcurso)
		print jurado_lst

		valfecha = not validarfechas(milestone.fecha_entrega,date.today())

		valigual = fechasiguales(milestone.fecha_entrega,date.today())
		print valigual

		if(request.session["tipo"]=="institucion"):
			valinst=True
		else:
			valinst=False

		args={}
		args['valinst']=valinst
		args['valigual']=valigual
		args['concurso']=concurso
		args['lstjurados']=jurado_lst
		args['milestone']=milestone
		args['valfecha']=valfecha
		return render_to_response('ajax_milestone.html',args,) 
	else:
		print 'no funcionaa' 
		return HttpResponseRedirect('/RNNotFound')
