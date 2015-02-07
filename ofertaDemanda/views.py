from django.shortcuts import render_to_response
from models import *

def Demandas(request):
    return render_to_response('DEMANDA_Inicio.html')

def DemandaCrear(request):
    return render_to_response('DEMANDA_crear_demanda.html')

def DemandaVer(request):
    return render_to_response('DEMANDA_perfil.html')


def Ofertas(request):
    return render_to_response('OFERTA_Inicio2.html')

def OfertaCrear(request):
    return render_to_response('OFERTA_crear_oferta.html')

def OfertaVer(request):
    return render_to_response('OFERTA_perfil.html')