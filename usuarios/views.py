# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from forms import UsuarioForm2
from django.contrib.auth.forms import UserCreationForm
from models import *

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
	return render_to_response('USUARIO_index.html')

def register(request):
	if request.method=='POST':
		form=UsuarioForm2(request.POST)
	
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/register_success/')
		else:
			print form.is_valid()
	else:
		form=UsuarioForm2()

	args={}
	args.update(csrf(request))
	
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

def perfil_view(request):
	id_session=request.session['id_user']
	print id_session
	user1=User.objects.get(id=id_session)
	#persona=
	return render_to_response('USUARIO_profile.html', {'full_name':user1.username})
