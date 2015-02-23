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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect


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
		#personas=Persona.objects.raw('SELECT * FROM persona WHERE user_ptr_id =%s',request.user.id)
		persona=Persona.objects.get(user_ptr=user)
		#p=personas[0]
		p=persona
		request.session['id_persona']=p.idpersona
		#print p.idpersona
		return HttpResponseRedirect('/perfil')
	else:
		return HttpResponseRedirect('/invalid')
	
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
	
	id_persona=request.session['id_persona']
	print id_session, id_persona
	user1=User.objects.get(id=id_session)
	persona1=Persona.objects.get(idpersona=id_persona)
	args={}
	args['usuario']=user1
	args['persona']=persona1
	
	return render_to_response('USUARIO_profile.html',args,context_instance=RequestContext(request))


@login_required(login_url='/ingresar/')
def enviar_mensaje(request):
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
					mensaje.fecha='2012-12-12'
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
		id_persona=request.session['id_persona']
		form1=MensajeForm()
	args={}
	args.update(csrf(request))
	args['form']=form1
	return render_to_response('USUARIO_enviar-mensaje.html',args)

@login_required(login_url='/ingresar/')
def mensajes_view(request):
	id_persona=request.session['id_persona']
	mensajes = Mensaje.objects.all().filter(idDestino=request.session['id_user'])[:8]
	args={}
	args['mensajes']=mensajes
	args['range']=range(len(mensajes))
	return render_to_response('USUARIO_inbox.html',args)

@login_required(login_url='/ingresar/')
def mensajesEnviados_view(request):
	id_persona=request.session['id_persona']
	mensajes = Mensaje.objects.all().filter(idEmisor=request.session['id_user'])[:8]
	args={}
	p=Persona.objects.get(idpersona=id_persona)
	args['mensajes']=mensajes
	args['persona']=p
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
	return render_to_response('404.html')



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

"""
@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_view(request):
	id_persona=request.session['id_persona']
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
			Q(first_name__icontains=name)

			)
		resultsUser=User.objects.filter(qset2).distinct()
		print "usrs", resultsUser
	else:
		results1 = []
		results2 = []
		results3 = []
		resultsUser=[]
		
	return render_to_response("USUARIO_busqueda.html",{
		"results1": results1,"results2": results2,"results3": results3,
		"resultsUser": resultsUser,
		 "name": name},
		context_instance = RequestContext(request))			

"""
@login_required(login_url='/ingresar/')
def verPerfil(request):
	idu = request.GET.get('q', '')
	user1=User.objects.get(username = idu)
	persona1=Persona.objects.get(user_ptr=user1)
	args = {}
	args['usuario']=user1
	args['persona']=persona1
	
	return render_to_response('USUARIO_profile.html',args,context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def verMensaje(request):
	args = {}
	try: 
		idM = int(request.GET.get('q', ''))
		msj=Mensaje.objects.get(id = idM)
		print "mensaje",msj.id
		user1=msj.idEmisor
		#print "user",user1
		persona=Persona.objects.get(user_ptr=user1)
		#print "persona",persona
		args['msj']=msj
		args['user1']=user1
		args['persona']=persona
		return render_to_response('USUARIO_verMensaje.html',args,context_instance=RequestContext(request))
	except:
		return HttpResponseRedirect("/mensajes/")
	
	return render_to_response('USUARIO_verMensaje.html',args,context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_view(request):
	

	id_persona=request.session['id_persona']
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
			Q(first_name__icontains=name)

			)
		resultsUser=User.objects.filter(qset2).distinct()
		print "usrs", resultsUser
	else:
		results1 = []
		results2 = []
		results3 = []
		resultsUser=[]
	tipo="Busqueda General"
	args={
		"results1": results1,"results2": results2,"results3": results3,
		"resultsUser": resultsUser,"name":name, "tipo":tipo}	

	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			



@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_oferta(request):
	
	id_persona=request.session['id_persona']
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
	tipo="Busqueda Ofertas"
	args={
		"results1": results1,
		 "name": name,
		 "tipo":tipo}	
	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_demanda(request):

	id_persona=request.session['id_persona']
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
	tipo="Busqueda Demanda"
	args={
		"results2": results2,
		 "name": name,
		 "tipo":tipo}	
	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			



@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_concursos(request):

	id_persona=request.session['id_persona']
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

	tipo="Busqueda Concursos"
	args={
		"results3": results3,
		 "name": name,
		 "tipo":tipo}	
		 
	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			


@login_required(login_url='/ingresar/')
@csrf_protect
def busqueda_usuario(request):

	id_persona=request.session['id_persona']
	name = request.GET.get('q','')
	if name:
		qset=(
			Q(first_name__icontains=name)

			)
		resultsUser=User.objects.filter(qset).distinct()
	else:
		resultsUser = []
	tipo="Busqueda Usuarios"
	args={
		"resultsUser": resultsUser,
		 "name": name,
		 "tipo":tipo}

	return render_to_response("USUARIO_busqueda.html",args,
		context_instance = RequestContext(request))			