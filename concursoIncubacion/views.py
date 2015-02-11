# Create your views here.
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from forms import *
from models import *
from usuarios.models import *
from app.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/ingresar/')
def homeConcursos(request):
    lst_concursos = Concurso.objects.all()[:8]
    return render_to_response('CONCURSO_inicio_concurso.html',{'lst_concursos' : lst_concursos},context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def crearConcurso(request): 
    info_enviado = False
    id_user=Persona.objects.get(idpersona=request.session['id_persona'])
    
    if request.method=='POST': #POST
        info_enviado = True
        form = crearConcursoForm(request.POST)

        if form.is_valid():
            #datos para publicacion
            Con = Concurso()
            Con.idusuario=Persona.objects.get(idpersona=request.session['id_persona'])
            Con.nombre=form.cleaned_data['nombre']
            Con.descripcion=form.cleaned_data['descripcion']
            Con.dominio=form.cleaned_data['dominio']
            Con.subdominio=form.cleaned_data['subdominio']
    
            #datos para detalle concursos
            Con.fecha_inicio=form.cleaned_data['fechainicio']
            Con.fecha_fin=form.cleaned_data['fechafin']
            Con.premios=form.cleaned_data['premios']
            Con.alcance=form.cleaned_data['alcance']
            Con.num_finalistas=form.cleaned_data['numfinalistas']
            Con.perfil=form.cleaned_data['perfil']
            Con.tipo_oferta=form.cleaned_data['tipooferta']
            Con.estado=1
            Con.save()
            info="Datos Guardados Correctamente"
        else:
            info="Informacion con datos incorrectos"

        form = crearConcursoForm()
        ctx = {'form':form,'info_enviado':info_enviado,'info':info,'id_user':id_user}
        return HttpResponseRedirect('/crearConcurso/',ctx)
        #return render_to_response('CONCURSO_crear_concurso.html',ctx,context_instance=RequestContext(request))

    else: #GET
        form = crearConcursoForm()
        ctx = {'form':form,'info_enviado':info_enviado,'id_user':id_user}
        return render_to_response('CONCURSO_crear_concurso.html',ctx,context_instance=RequestContext(request))

@login_required(login_url='/ingresar/')
def verConcurso(request):
    return render_to_response('CONCURSO_perfil.html')

@login_required(login_url='/ingresar/')
def homeIncubacion(request):
    return render_to_response('INCUBACION_inicio.html')
    
@login_required(login_url='/ingresar/')
def verIncubacion(request):
    return render_to_response('INCUBACION_perfil.html')
    
@login_required(login_url='/ingresar/')    
def crearIncubacion(request):
    return render_to_response('INCUBACION_crear.html')    # Create your views here.
