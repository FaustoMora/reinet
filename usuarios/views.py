# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import *
from django.contrib.auth.forms import UserCreationForm
from models import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

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
            persona=Persona.objects.get(user_ptr=user)
            p=persona
            request.session['id_persona']=p.idpersona
            redir='/perfil'
        except ObjectDoesNotExist:
            request.session['id_institucion']=Institucion.objects.get(user_ptr=request.user).idinstitucion
            redir='/'
        return HttpResponseRedirect(redir)
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
			userReceptor=User.objects.get(username=ur)
			print "aqui ureceptor",userReceptor
			#receptor=Persona.objects.get(id_user)
			mensaje.idEmisor=emisor
			mensaje.idDestino=emisor
			mensaje.fecha='2012-12-12'
			mensaje.hora='12:00:00'
			mensaje.save()
			return HttpResponseRedirect('/mensajes/')
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
	return render_to_response('USUARIO_inbox.html',args)

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



	
