# -*- encoding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from models import *
from ofertaDemanda.models import *
from concursoIncubacion.models import *
from incubacion.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from datetime import datetime

def index(request):
	return render_to_response('USUARIO_index.html')


def ingresar(request):
	c={}
	c.update(csrf(request))
	return render_to_response('USUARIO_sign-in.html',c)


def auth_view(request):
	name=request.POST.get('Email', '')
	password=request.POST.get('password', '')
	user=auth.authenticate(username=name, password=password)
		
	if user is not None:
		auth.login(request, user)
		request.session['id_user']=request.user.id
		user=User.objects.get(id=request.user.id)
		try:
			print "entro persona"
			#Persona
			persona=Persona.objects.get(user_ptr=user)	
		except Persona.DoesNotExist:
			persona=None
		try:
			print "entro inst"
			#Institucion
			institucion=Institucion.objects.get(user_ptr=user)
		except Institucion.DoesNotExist:
			institucion=None

		if persona is not None:
			print "asigno persona"
			p=persona
			request.session['id_persona']=p.idpersona
			request.session['tipo']="persona"
			return HttpResponseRedirect('/inicio_view')
		elif institucion is not None:
			ins=institucion
			request.session['id_institucion']=ins.idinstitucion
			request.session['tipo']="institucion"
			return HttpResponseRedirect('/inicio_view')	
		else:
			return HttpResponseRedirect('/invalid')	

	else:
		c={}
		c['fallaLogin']="Usuario o Contraseña incorrectos"
		c.update(csrf(request))
		return render_to_response('USUARIO_sign-in.html',c)

def loggedin(request):
	print request.session['id_user']
	return render_to_response('USUARIO_profile.html', {'full_name': request.user.username})
	
def invalid(request):
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	return render_to_response('base.tpl.html')

def register(request):
	if request.method=='POST':
		form=PersonaForm(request.POST, request.FILES)
	
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/ingresar/')
		else:
			print form.is_valid()
	else:
		form=PersonaForm()

	args={}
	args.update(csrf(request))
	for f in form:
		print f.id_for_label
	args['form']=form
	return render_to_response('USUARIO_sign-up.html', args)


def register_success(request):
	return render_to_response('USUARIO_index.html')


def create(request):
	if request.POST:
		form=UsuarioForm2(request.POST)
		if form.is_valid():
			form.save()			
			return HttpResponseRedirect('/usuarios/all')	
	else:
		form=UsuarioForm2()
	
	args={}
	args.update(csrf(request))
	args['form']= form
	return render_to_response('USUARIO_sign-up.html', args)


@login_required(login_url='/ingresar/')
def perfil_view(request):
	id_session=request.session['id_user']
	tipo = request.session['tipo']
	user1=User.objects.get(id=id_session)

	if tipo == "persona":
		id_persona=request.session['id_persona']
		persona1=Persona.objects.get(idpersona=id_persona)
		institucion1=None
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
		institucion1=Institucion.objects.get(idinstitucion=id_institucion)
		persona1=None

	args={}
	args['usuario']=user1
	if persona1 is not None:
		args['persona']=persona1
		return render_to_response('USUARIO_profile.html',args,context_instance=RequestContext(request))
	else:
		args['institucion']=institucion1
		return render_to_response('USUARIO_perfilinstitucion.html',args,context_instance=RequestContext(request))
	


@login_required(login_url='/ingresar/')
def enviar_mensaje(request):
	tipo = request.session['tipo']
	id_user=request.session['id_user']
	if request.method=='POST':
		form1=MensajeForm(request.POST)
		if form1.is_valid():
			mensaje=super(MensajeForm,form1).save(commit=False)
			emisor=User.objects.get(id=id_user)
			ur=form1.cleaned_data['recibe']
			print "aqui ur",ur
			try:
				userReceptor=User.objects.get(username=ur)
				print "aqui ureceptor",userReceptor, "envia", emisor
				if userReceptor is not None:
					#receptor=Persona.objects.get(id_user)
					mensaje.idEmisor=emisor
					mensaje.idDestino=userReceptor
					mensaje.fecha=datetime.now()
					mensaje.hora='12:00:00'
					mensaje.leido='0'
					mensaje.save()
					return HttpResponseRedirect('/mensajesEnviados/')
				else:
					print "usuari no valido"
					form1=MensajeForm()
			except:
				print "usuari no valido"
				form1=MensajeForm()
	else:
		if tipo == "persona":
			id_persona=request.session['id_persona']		
		elif tipo == "institucion":
			id_institucion=request.session['id_institucion']
		form1=MensajeForm()
	args={}
	args.update(csrf(request))
	args['form']=form1
	return render_to_response('USUARIO_enviar-mensaje.html',args)


@login_required(login_url='/ingresar/')
def mensajes_view(request):
	tipo=request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']

	mensajes = Mensaje.objects.all().filter(idDestino=request.session['id_user'])[:8]
	args={}
	args['mensajes']=mensajes
	args['range']=range(len(mensajes))
	return render_to_response('USUARIO_inbox.html',args)


@login_required(login_url='/ingresar/')
def mensajesEnviados_view(request):
	tipo = request.session['tipo']

	if tipo == "persona":
		id_persona=request.session['id_persona']
		persona1=Persona.objects.get(idpersona=id_persona)
		institucion1=None
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
		institucion1=Institucion.objects.get(idinstitucion=id_institucion)
		persona1=None
	mensajes = Mensaje.objects.all().filter(idEmisor=request.session['id_user'])[:8]
	args={}
	args['mensajes']=mensajes
	if persona1 is not None:
		args['persona']=persona1	
	else:
		args['institucion']=institucion1
	return render_to_response('USUARIO_enviados.html',args)


@login_required(login_url='/ingresar/')
def inicio_view(request):
        id_session=request.session['id_user']
        return render_to_response('USUARIO_inicio.html')


@login_required(login_url='/ingresar/')
def editar_perfil_view(request):
	id_session=request.session['id_user']
	id_persona=request.session['id_persona']
	args={}
	if request.method == 'POST':
		id_session=request.session['id_user']
		id_persona=request.session['id_persona']
		#user=User.objects.get(id=id_session)
		persona=Persona.objects.get(idpersona=id_persona)
		#user_form = UserCreationForm(request.POST,  request.FILES,instance=user)
		persona_form = PersonaEditarForm(request.POST, request.FILES, instance=persona)
		print "validacioneees", persona_form.is_valid()
		if  persona_form.is_valid():
			#user_form.save()
			persona_form.save()
			return HttpResponseRedirect('/perfil/')
		else:
			#user=User.objects.get(id=id_session)
			persona=Persona.objects.get(idpersona=id_persona)
			#user_form = UserCreationForm(instance=user)
			persona_form = PersonaEditarForm(instance=persona)
			#args['userform']=user_form
			args['personaform']=persona_form
	else:
		#user=User.objects.get(id=id_session)
		persona=Persona.objects.get(idpersona=id_persona)
		#user_form = UserCreationForm(instance=user)
		persona_form = PersonaEditarForm(instance=persona)
		#args['userform']=user_form
		args['personaform']=persona_form
	#return render_to_response('USUARIO_edit-profile.html', args)
	return render_to_response('USUARIO_edit-profile.html', RequestContext(request,args))


def my_404_view(request):
	try:
		id_session=request.session['id_user']
	except:
		id_session=None
	args={}
	if id_session is not None:
		tipo404="inicio_view"
	else:
		tipo404="index"
	args['tipo404']=tipo404
	return render_to_response('404.html',args,context_instance=RequestContext(request))


@login_required(login_url='/ingresar/')
def subir_imagen(request):
	id_persona=request.session['id_persona']
	persona=Persona.objects.get(idpersona=id_persona)
	if request.method == 'POST':
		persona_form=ImagenPerfilForm(request.POST,request.FILES, instance=persona)
		if persona_form.is_valid():
			persona_form.save()
			return HttpResponseRedirect('/perfil/')
		else:
			persona=Persona.objects.get(idpersona=id_persona)
			persona_form = PersonaEditarForm(instance=persona)
			args['personaform']=persona_form


@login_required(login_url='/ingresar/')
def verPerfil(request):
	idu = request.GET.get('q', '')
	try:
		user1=User.objects.get(username = idu)
		args={}
		args['usuario']=user1
		tipo = request.session['tipo']
		try:
			print "persona perfil otro"
			persona1=Persona.objects.get(user_ptr=user1)
			args['persona']=persona1
			return render_to_response('USUARIO_perfilOtro.html',args,context_instance=RequestContext(request))
		except:
			institucion1=Institucion.objects.get(user_ptr=user1)
			args['institucion']=institucion1
			return render_to_response('USUARIO_perfilinstitucionOtro.html',args,context_instance=RequestContext(request))
	except:
		return HttpResponseRedirect('/RNNotFound/')	
@login_required(login_url='/ingresar/')
def verMensaje(request):
	args = {}
	tipo = request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
		yo=Persona.objects.get(idpersona=id_persona)
		
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
		yo=Institucion.objects.get(idinstitucion=id_institucion)
	
	args['yo']=yo
	try: 
		idM = int(request.GET.get('q', ''))
		msj=Mensaje.objects.get(id = idM)
		print "mensaje",msj.id
		user1=msj.idEmisor
		#print "user",user1
		#persona=Persona.objects.get(user_ptr=user1)
		#print "persona",persona
		args['msj']=msj
		args['user1']=user1
		#args['persona']=persona
		
		return render_to_response('USUARIO_verMensaje.html',args,context_instance=RequestContext(request))
	except:
		return HttpResponseRedirect("/mensajes/")
	
	return render_to_response('USUARIO_verMensaje.html',args,context_instance=RequestContext(request))


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_view(request):
	"""
	tipo = request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
		
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
	"""
	name = request.GET.get('q','')
	print "funciona",name
	if name:
		qset = (
			Q(nombre__icontains=name)|
			Q(dominio__icontains=name)
		)
		results1 = Oferta.objects.filter(qset).distinct()
		results2 = Demanda.objects.filter(qset).distinct()
		results3 = Concurso.objects.filter(qset).distinct()
		qset2=(
			Q(first_name__icontains=name)|
			Q(last_name__icontains=name)|
			Q(username__icontains=name)
			)
		resultsUser=User.objects.filter(qset2).distinct()
		print "usrs", resultsUser
	else:
		results1 = []
		results2 = []
		results3 = []
		resultsUser=[]
	tipoB="Busqueda General"
	linkTipo="busqueda"
	args={
		"results1": results1,"results2": results2,"results3": results3,
		"resultsUser": resultsUser,"name":name, "tipoB":tipoB,
		"linkTipo":linkTipo}
	print resultsUser	

	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_oferta(request):
	
	tipo = request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
		
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
	name = request.GET.get('q','')
	print "funciona",name
	if name:
		qset = (
			Q(nombre__icontains=name)|
			Q(dominio__icontains=name)
		)
		results1 = Oferta.objects.filter(qset).distinct()
	else:
		results1 = []
	tipoB="Busqueda Ofertas"
	linkTipo="busquedaOferta"
	args={
		"results1": results1,
		 "name": name,
		 "tipoB":tipoB,
		 "linkTipo":linkTipo}	
	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_demanda(request):

	tipo = request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
		
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
	name = request.GET.get('q','')
	print "funciona",name
	if name:
		qset = (
			Q(nombre__icontains=name)|
			Q(dominio__icontains=name)
		)
		results2 = Demanda.objects.filter(qset).distinct()
	else:
		results2 = []
	tipoB="Busqueda Demanda"
	linkTipo="busquedaDemanda"
	args={
		"results2": results2,
		 "name": name,
		 "tipoB":tipoB,
		 "linkTipo":linkTipo}	
	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_concursos(request):

	tipo = request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
		
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
	name = request.GET.get('q','')
	print "funciona",name
	if name:
		qset = (
			Q(nombre__icontains=name)|
			Q(dominio__icontains=name)
		)
		results3 = Concurso.objects.filter(qset).distinct()
	else:
		results3 = []

	tipoB="Busqueda Concursos"
	linkTipo="busquedaConcurso"
	args={
		"results3": results3,
		 "name": name,
		 "tipoB":tipoB,
		 "linkTipo":linkTipo}	
		 
	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_usuario(request):

	tipo = request.session['tipo']
	if tipo == "persona":
		id_persona=request.session['id_persona']
		
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
	name = request.GET.get('q','')
	if name:
		qset=(
			Q(first_name__icontains=name)|
			Q(last_name__icontains=name)|
			Q(username__icontains=name)
			)
		resultsUser=User.objects.filter(qset).distinct()
	else:
		resultsUser = []
	tipoB="Busqueda Usuarios"
	linkTipo="busquedaUsuario"
	args={
		"resultsUser": resultsUser,
		 "name": name,
		 "tipoB":tipoB,
		 "linkTipo":linkTipo}

	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			

"""VISTAS DE INSTITUCION"""

def registerInst(request):
	if request.method=='POST':
		form1=InstitucionForm(request.POST, request.FILES)
	
		if form1.is_valid():
			form1.save()
			return HttpResponseRedirect('/ingresar/')
		else:
			print form1.is_valid()
	else:
		form1=InstitucionForm()

	args={}
	args.update(csrf(request))
	for fi in form1:
		print fi.id_for_label
	args['form1']=form1
	return render_to_response('USUARIO_creaInstitucion.html', args)


@login_required(login_url='/ingresar/')
def perfil_institucion(request):
	id_session=request.session['id_user']
	
	id_institucion=request.session['id_institucion']
	print id_session, id_institucion
	user1=User.objects.get(id=id_session)
	institucion1=Institucion.objects.get(idinstitucion=id_institucion)
	args={}
	args['usuario']=user1
	args['institucion']=institucion1
	
	return render_to_response('USUARIO_perfilinstitucion.html',args,context_instance=RequestContext(request))


@login_required(login_url='/ingresar/')
def editar_perfil_institucion(request):
	id_session=request.session['id_user']
	id_institucion=request.session['id_institucion']
	args={}
	if request.method == 'POST':
		id_session=request.session['id_user']
		id_institucion=request.session['id_institucion']
		#user=User.objects.get(id=id_session)
		institucion=Institucion.objects.get(idinstitucion=id_institucion)
		#user_form = UserCreationForm(request.POST,  request.FILES,instance=user)
		institucion_form = InstitucionEditarForm(request.POST, request.FILES, instance=institucion)
		print "validacioneees", institucion_form.is_valid()
		if  institucion_form.is_valid():
			#user_form.save()
			institucion_form.save()
			return HttpResponseRedirect('/perfilInst/')
		else:
			#user=User.objects.get(id=id_session)
			institucion=Institucion.objects.get(idinstitucion=id_institucion)
			#user_form = UserCreationForm(instance=user)
			institucion_form = InstitucionEditarForm(instance=institucion)
			#args['userform']=user_form
			args['institucionform']=institucion_form
	else:
		#user=User.objects.get(id=id_session)
		institucion=Institucion.objects.get(idinstitucion=id_institucion)
		#user_form = UserCreationForm(instance=user)
		institucion_form = InstitucionEditarForm(instance=institucion)
		#args['userform']=user_form
		args['institucionform']=institucion_form
	#return render_to_response('USUARIO_edit-profile.html', args)
	return render_to_response('USUARIO_edit-profile-institucion.html', RequestContext(request,args))


@login_required(login_url='/ingresar/')
def verInicioF(request):
	id_session=request.session['id_user']
	tipo = request.session['tipo']

	user1=User.objects.get(id=id_session)
	if tipo == "persona":
		id_persona=request.session['id_persona']
		persona1=Persona.objects.get(idpersona=id_persona)
		institucion1=None
	elif tipo == "institucion":
		id_institucion=request.session['id_institucion']
		institucion1=Institucion.objects.get(idinstitucion=id_institucion)
		persona1=None
		
	lst_concursos = Concurso.objects.all()
	lst_demandas = Demanda.objects.all()
	lst_ofertas = Oferta.objects.all()
	lst_incubaciones = Incubacion.objects.all()
	print "demandas",lst_demandas
	print "ofertas", lst_ofertas
	args={"lst_concursos":lst_concursos,"lst_demandas":lst_demandas,
		 "lst_ofertas":lst_ofertas,"lst_incubaciones":lst_incubaciones,
		 "usuario":user1}
	if persona1 is not None:
		args['persona']=persona1	
	else:
		args['institucion']=institucion1

	return render_to_response('USUARIO_inicioF.html',args,context_instance=RequestContext(request))


def terminos(request):
	return render_to_response("terms.html")



"""VISTAS INDEX """

def ofertaSinLogin(request):
	lst_ofertas = Oferta.objects.all()
	args={"lst_ofertas":lst_ofertas}
	return render_to_response('USUARIO_ofertaSinLogin.html',args,context_instance=RequestContext(request))

def demandaSinLogin(request):
	lst_demandas = Demanda.objects.all()
	args={"lst_demandas":lst_demandas}
	return render_to_response('USUARIO_demandaSinLogin.html',args,context_instance=RequestContext(request))

def concursoSinLogin(request):
	lst_concursos = Concurso.objects.all()
	args={"lst_concursos":lst_concursos}
	return render_to_response('USUARIO_concursoSinLogin.html',args,context_instance=RequestContext(request))

def incubacionSinLogin(request):
	lst_incubaciones = Incubacion.objects.all()
	args={"lst_incubaciones":lst_incubaciones}
	return render_to_response('USUARIO_incubacionSinLogin.html',args,context_instance=RequestContext(request))

def institucionSinLogin(request):
	lst_inst = Institucion.objects.all()
	args={"lst_inst":lst_inst}
	return render_to_response('USUARIO_institucionSinLogin.html',args,context_instance=RequestContext(request))