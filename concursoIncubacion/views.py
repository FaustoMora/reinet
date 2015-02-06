# Create your views here.
from django.shortcuts import render
from django.shortcuts import render_to_response
from forms import crearConcurso
from models import Publicacion
from models import DetalleConcurso


def homeConcursos(request):
	return render_to_response('CONCURSO_inicio_concurso.html')

def crearConcurso(request):
	return render_to_response('CONCURSO_crear_concurso.html')

def verConcurso(request):
	return render_to_response('CONCURSO_perfil.html')

def homeIncubacion(request):
	return render_to_response('INCUBACION_inicio.html')
	
def verIncubacion(request):
	return render_to_response('INCUBACION_perfil.html')
	
def crearIncubacion(request):
	return render_to_response('INCUBACION_crear.html')	