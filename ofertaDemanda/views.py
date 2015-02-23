from django.shortcuts import render_to_response, render
from django.core.files import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from models import *
from usuarios.models import *
from app.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.context_processors import csrf
from forms import *
from django.db.models import Q
from django.forms.util import ValidationError
from django.core.urlresolvers import reverse

@login_required(login_url='/ingresar/') 
def homeDemandas(request):
    persona = Persona.objects.get(idpersona=request.session['id_persona'])
    lst_demandas = Demanda.objects.filter(~Q(idusuario = request.session['id_persona']))[:8]
    return render_to_response('DEMANDA_Inicio.html',{'lst_demandas': lst_demandas,'persona':persona},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/') 
def verDemanda(request):
    return render_to_response('DEMANDA_perfil.html')

@login_required(login_url='/ingresar/') 
def misDemandas(request):
    persona = Persona.objects.get(idpersona=request.session['id_persona'])
    lst_demandas = Demanda.objects.filter(idusuario = request.session['id_persona'])[:5]
    return render_to_response('DEMANDA_mis_Demanda.html', {'lst_demandas' :lst_demandas,'persona':persona}, context_instance=RequestContext(request)) 

@login_required(login_url='/ingresar/') 
def homeOfertas(request):
    persona = Persona.objects.get(idpersona=request.session['id_persona'])
    lst_ofertas = Oferta.objects.filter(~Q(idusuario = request.session['id_persona']))[:8]
    return render_to_response('OFERTA_Inicio2.html',{'lst_ofertas': lst_ofertas,'persona':persona},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearOferta(request):
    form = CrearOfertaForm(request.POST, request.FILES)
    if form.is_valid():
        nuevaOferta=super(CrearOfertaForm, form).save(commit=False)
        nuevaOferta.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
        nuevaOferta.estadoOferta=1
        nuevaOferta.ofertaPublicada =1            
        nuevaOferta.save()
        return HttpResponseRedirect(reverse('completarOferta', args=(nuevaOferta.idOferta,)))
        #return HttpResponseRedirect(reverse('completarOferta', args=(),kwargs={'ofertaid': nuevaOferta.idOferta}))
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('OFERTA_crear_oferta.html',args)

@login_required(login_url='/ingresar/')
def completarOferta(request,ofertaid):
    ofertaCompletar=Oferta.objects.get(idOferta = ofertaid)
    form = CompletarOfertaForm(request.POST, request.FILES, instance=ofertaCompletar)
    if form.is_valid():
        return HttpResponseRedirect('/misOfertas/')

    args={}
    args.update(csrf(request))
    args['form']=form
    args['oferta']=Oferta.objects.get(idOferta=ofertaid)
    return render_to_response('OFERTA_crear_oferta_completar.html', args, context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearDiagramaCanvas(request,ofertaid):
    form = CanvasForm(request.POST, request.FILES)
    if form.is_valid():
        return HttpResponseRedirect('/misOfertas/')

    args={}
    args.update(csrf(request))
    args['form']=form
    args['oferta']=Oferta.objects.get(idOferta=ofertaid)
    return render_to_response('OFERTA_crear_oferta_completar.html', args, context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearDiagramaPorter(request,ofertaid):
    form = PorterForm(request.POST, request.FILES)
    if form.is_valid():
        return HttpResponseRedirect('/misOfertas/')

    args={}
    args.update(csrf(request))
    args['form']=form
    args['oferta']=Oferta.objects.get(idOferta=ofertaid)
    return render_to_response('OFERTA_crear_oferta_completar.html', args, context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearDemanda(request):
    form = CrearDemandaForm(request.POST, request.FILES)

    if form.is_valid():
        nuevaDemanda=super(CrearDemandaForm, form).save(commit=False)
        nuevaDemanda.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
        nuevaDemanda.estadoDemanda=1
        nuevaDemanda.save()
        return HttpResponseRedirect('/misDemandas/',nuevaDemanda.idDemanda)

    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('DEMANDA_crear_demanda.html',args)    
	
@login_required(login_url='/ingresar/') 
def verOferta(request):
    return render_to_response('OFERTA_perfil.html')


@login_required(login_url='/ingresar/') 
def editarOferta(request):    
    return render_to_response('OFERTA_perfil.html')


@login_required(login_url='/ingresar/') 
def misOfertas(request):
    persona = Persona.objects.get(idpersona=request.session['id_persona'])
    lst_ofertas = Oferta.objects.filter(idusuario = request.session['id_persona'])[:5]
    return render_to_response('OFERTA_misOfertas.html', {'lst_ofertas' :lst_ofertas,'persona':persona}, context_instance=RequestContext(request)) 

def search(request):
    errors= []
    if 'busquedaOfertaRed' in request.GET:
        busquedaOfertaRed = request.GET['busquedaOfertaRed']
        if not busquedaOfertaRed:
            errors.append('Ingrese un termino a buscar')
        elif len(busquedaOfertaRed)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            ofertas = Oferta.objects.filter(nombre__icontains=busquedaOfertaRed)
            return render(request, 'OFERTA_Inicio2.html',
                {'ofertas':ofertas,'nombre':busquedaOfertaRed,'buscarOfer':True})
        return render(request,'OFERTA_Inicio2.html',{'errors':errors})    


def searchDemanda(request):
    errors= []
    if 'busquedaDemandaRed' in request.GET:
        busquedaDemandaRed = request.GET['busquedaDemandaRed']
        if not busquedaDemandaRed:
            errors.append('Ingrese un termino a buscar')
        elif len(busquedaDemandaRed)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            demandas = Demanda.objects.filter(nombre__icontains=busquedaDemandaRed)
            return render(request, 'DEMANDA_Inicio.html',
                {'demandas':demandas,'nombre':busquedaDemandaRed,'buscarDema':True})
        return render(request,'DEMANDA_Inicio.html',{'errors':errors})