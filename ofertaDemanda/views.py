from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from models import *

def DemandaInicio(request):
    return render_to_response('DEMANDA_Inicio.html')

def OfertaInicio(request):
    return render_to_response('OFERTA_Inicio.html')
