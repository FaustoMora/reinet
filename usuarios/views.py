# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render

def index(request):
	return render_to_response('USUARIO_index.html')

def ingresar(request):
	return render_to_response('USUARIO_sign-in.html')

