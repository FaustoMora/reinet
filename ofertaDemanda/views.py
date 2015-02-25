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
    tipo_user = request.session['tipo']
    print tipo_user
    if tipo_user=="persona":
        persona = Persona.objects.get(idpersona=request.session['id_persona'])
        lst_demandas = Demanda.objects.filter(~Q(idusuario = request.session['id_user']))[:8]
        return render_to_response('DEMANDA_Inicio.html',{'lst_demandas': lst_demandas,'persona':persona,'tipo_user':tipo_user},context_instance=RequestContext(request))
    elif tipo_user=="institucion":
        lst_demandas = Demanda.objects.all()[:8]
    return render_to_response('DEMANDA_Inicio.html',{'lst_demandas': lst_demandas,'tipo_user':tipo_user},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/') 
def verDemanda(request):
    iddem = int(request.GET.get('q', ''))
    demanda=Demanda.objects.get(idDemanda = iddem)
    imagenes= ImagenDemanda.objects.all().filter(idDemanda = iddem)
    demandaUsuario=Demanda.objects.get(idDemanda = iddem).idusuario.id
	
    args = {}
    args['demanda'] = demanda

    if (demandaUsuario == request.session['id_user']):
	    val = True;
    else:
	    val = False;
    print "Probado"
    print demandaUsuario
    print request.session['id_user']
    print val
    args['val'] = val
    args['imagenes'] = imagenes
    args['nums'] = range(len(imagenes))
    return render_to_response('DEMANDA_perfil.html', args)

@login_required(login_url='/ingresar/') 
def misDemandas(request):
    persona = Persona.objects.get(idpersona=request.session['id_persona'])
    lst_demandas = Demanda.objects.filter(idusuario = request.session['id_user'])[:5]
    print lst_demandas
    return render_to_response('DEMANDA_mis_Demanda.html', {'lst_demandas' :lst_demandas,'persona':persona}, context_instance=RequestContext(request)) 

@login_required(login_url='/ingresar/') 
def homeOfertas(request):
    tipo_user = request.session['tipo']
    if tipo_user=="persona":
        persona = Persona.objects.get(idpersona=request.session['id_persona'])
        lst_ofertas = Oferta.objects.filter(~Q(idusuario = request.session['id_user']))[:8]
        return render_to_response('OFERTA_Inicio2.html',{'lst_ofertas': lst_ofertas,'persona':persona,'tipo_user':tipo_user},context_instance=RequestContext(request))
    elif tipo_user=="institucion":
        lst_ofertas = Oferta.objects.all()[:8]
    return render_to_response('OFERTA_Inicio2.html',{'lst_ofertas': lst_ofertas,'tipo_user':tipo_user},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearOferta(request):
    if request.POST: #POST
        form = CrearOfertaForm(request.POST, request.FILES)

        if form.is_valid():
            nuevaOferta=super(CrearOfertaForm, form).save(commit=False)
            nuevaOferta.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
            nuevaOferta.estadoOferta=1
            nuevaOferta.ofertaPublicada =1 
            nuevaOferta.recienCreada=True          
            nuevaOferta.save()
                       
            info="Oferta creada correctamente"
        else:
            info="Error al ingresar los datos"

        form = CrearOfertaForm()
        messages.success(request, info)
        return HttpResponseRedirect('/misOfertas')
    else:
        form=CrearOfertaForm()

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
        print "todo esta bien"
        return HttpResponseRedirect('/misDemandas/')
    else:
        print "algo paso"
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response('DEMANDA_crear_demanda.html',args)    
	
@login_required(login_url='/ingresar/')
def verOferta(request):
    idof = int(request.GET.get('q', ''))
    oferta=Oferta.objects.get(idOferta = idof)
    imagenes= ImagenOferta.objects.all().filter(idOferta = idof)
    ofertaUsuario=Oferta.objects.get(idOferta = idof).idusuario.id
	
    args = {}
    args['oferta'] = oferta

    if (ofertaUsuario == request.session['id_user']):
	    val = True;
    else:
	    val = False;
    print "Probado"
    print ofertaUsuario
    print request.session['id_user']
    print val
    args['val'] = val
    args['imagenes'] = imagenes
    args['nums'] = range(len(imagenes))
    return render_to_response('OFERTA_perfil.html', args)

@login_required(login_url='/ingresar/') 
def editarOferta(request):    
    return render_to_response('OFERTA_perfil.html')


@login_required(login_url='/ingresar/') 
def misOfertas(request):
    persona = Persona.objects.get(idpersona=request.session['id_persona'])
    lst_ofertas = Oferta.objects.filter(idusuario = request.session['id_user'])[:5]
    return render_to_response('OFERTA_misOfertas.html', {'lst_ofertas' :lst_ofertas,'persona':persona}, context_instance=RequestContext(request)) 

def searchOfertaRed(request):
    errors= []
    if 'busquedaOfertaRed' in request.GET:
        busquedaOfertaRed = request.GET['busquedaOfertaRed']
        if not busquedaOfertaRed:
            errors.append('Ingrese un termino a buscar')
        elif len(busquedaOfertaRed)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            ofertas = Oferta.objects.filter(nombre__icontains=busquedaOfertaRed).exclude(idusuario = request.session['id_persona'])
            return render(request, 'OFERTA_Inicio2.html',
                {'ofertas':ofertas,'nombre':busquedaOfertaRed,'buscarOfer':True})
        return render(request,'OFERTA_Inicio2.html',{'errors':errors})    


def searchDemandaRed(request):
    errors= []
    if 'busquedaDemandaRed' in request.GET:
        busquedaDemandaRed = request.GET['busquedaDemandaRed']
        if not busquedaDemandaRed:
            errors.append('Ingrese un termino a buscar')
        elif len(busquedaDemandaRed)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            demandas = Demanda.objects.filter(nombre__icontains=busquedaDemandaRed).exclude(idusuario = request.session['id_persona'])
            return render(request, 'DEMANDA_Inicio.html',
                {'demandas':demandas,'nombre':busquedaDemandaRed,'buscarDema':True})
        return render(request,'DEMANDA_Inicio.html',{'errors':errors})



def searchMisOferta(request):
    errors= []
    if 'busquedaMisOferta' in request.GET:
        busquedaMisOferta = request.GET['busquedaMisOferta']
        if not busquedaMisOferta:
            errors.append('Ingrese un termino a buscar')
        elif len(busquedaMisOferta)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            ofertas = Oferta.objects.filter(nombre__icontains=busquedaMisOferta).filter(idusuario = request.session['id_persona'])
            return render(request, 'OFERTA_misOfertas.html',
                {'ofertas':ofertas,'nombre':busquedaMisOferta,'buscarMisOfer':True,'mostrarOfertas':False})
        return render(request,'OFERTA_misOfertas.html',{'errors':errors})    


def searchMisDemanda(request):
    errors= []
    if 'busquedaMisDemanda' in request.GET:
        busquedaMisDemanda = request.GET['busquedaMisDemanda']
        if not busquedaMisDemanda:
            errors.append('Ingrese un termino a buscar')  
        elif len(busquedaMisDemanda)>25:
            errors.append('por favor ingrese un termino no mas de 25 caracteres.')
        else:
            demandas = Demanda.objects.filter(nombre__icontains=busquedaMisDemanda).filter(idusuario = request.session['id_persona'])
            return render(request, 'DEMANDA_mis_Demanda.html',
                {'demandas':demandas,'nombre':busquedaMisDemanda,'buscarMisDema':True,'mostrarDemanda':False})
        return render(request,'DEMANDA_mis_Demanda.html',{'errors':errors})