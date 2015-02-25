'''
Created on 11/2/2015

@author: Dark Legion
'''
from django import forms
from app.models import *
from models import *
from usuarios.models import Persona

from django.db import models

from usuarios.models import *
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import datetime






class CrearOfertaForm(forms.ModelForm):
    
    class Meta:
        model = Oferta
        fields = ['tipoOferta','nombre','imagen','descripcion','dominio','subdominio',
        'palabras_claves','lugar_aplicacion','tiempo_inicio_disponible',
        'tiempo_fin_disponible','perfil_beneficiario','perfil_cliente',
        'soluciones_alternativas','propuesta_valor','cuadro_competidores',
        'cuadro_tendencias_relevantes','estado_propiedad_intelectual','evidencia_traccion']
        labels = {
            #'nombre': _('Writer'),
        }
        help_texts = {
            #'nombre': _('Some useful help text.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("Debe escribir un nombre corto"),
            },
        }

    tipoOferta = forms.ChoiceField(
        label="Tipo de la oferta",
        choices = (
            ('1', "Emprendimiento"), 
            ('2', "Prototipo"),
            ('3', "Tecnologia")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '1',
    )

    nombre = forms.CharField(
        label="Nombre",
        max_length=150,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':'true'}
        )
    )

    descripcion = forms.CharField(
        max_length=500,
        label="Descripcion",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese una descripcion general de su oferta','rows':'4','style':'resize:none', 'required':'true'}
        )
    )

    dominio = forms.CharField(
        label="Dominio",
       # max_length=500,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':'true'}
        )
    )

    subdominio = forms.CharField(
        label="Subdominio",
        #max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':'true'}
        )
    )

    palabras_claves = forms.CharField(
        label="Palabras Claves",
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese palabras claves que se refieran a su oferta', 'required':'true'}
        )
    )

    lugar_aplicacion = forms.ChoiceField(
        label="Lugar de Aplicacion",
        choices = (
            ('1', "Azuay"),('2', "Bolivar"),('3', "Caniar"),
            ('4', "Carchi"),('5', "Chimborazo"),('6', "Cotopaxi"),('7', "El Oro"),
            ('8', "Esmeraldas"),('9', "Galapagos"),('10', "Guayas"),('11', "Imbabura"),
            ('12', "Loja"),('13', "Los Rios"),('14', "Manabi"),('15', "Morona Santiago"),
            ('16', "Napo"),('17', "Orellana"),('18', "Pastaza"),('19', "Pichincha"),
            ('20', "Santa Elena"),('21', "Santo Domingo de los Tsachilas"),('22', "Sucumbios"),('23', "Tungurahua"),('24', "Zamora Chinchipe")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':'true'}
            ),
        initial = '1',
    )

    tiempo_inicio_disponible = forms.DateField(

        label="Desde",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'true','type':'date'}
        )
    )

    tiempo_fin_disponible = forms.DateField(
        label="Hasta",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'true','type':'date'}
        )
    ) 


    perfil_beneficiario = forms.CharField(
        label="Perfil del Beneficiario",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los beneficiarios de su oferta si esta saliera al mercado','rows':'3','style':'resize:none'}
        )
    )

    perfil_cliente = forms.CharField(
        required=False,
        max_length=500,
        label="Perfil del Cliente",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los clientes de su oferta si esta saliera al mercado','rows':'3','style':'resize:none','required':'false'}
        )
    )

    soluciones_alternativas = forms.CharField(
        label="Soluciones Alternativas",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'4','style':'resize:none','required':'False'}
        )
    )

    propuesta_valor = forms.CharField(
        required=False,
        label="Propuestas de Valor",
        max_length=300,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'3','style':'resize:none','required':'false'}
        )
    )

    estado_propiedad_intelectual = forms.CharField(
        required=False,
        label="Estado Propiedad Intelectual",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'4','style':'resize:none','required':'false'}
        )
    )

    evidencia_traccion = forms.CharField(
        required=False,
        label="Evidencia de traccion",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Explique la evidencia de Traccion','rows':'4','style':'resize:none','required':'false'}
        )
    )   

    cuadroCompetidores = forms.CharField(
        label="Cuadro de Competidores",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Competidores','rows':'5','style':'resize:none','required':'false'}
        )
    )

    cuadroTendenciasRelativas = forms.CharField(
        label="Cuadro de Tendencias Relativas",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Tendencias Relativas','rows':'5','style':'resize:none','required':'false'}
        )
    )

    def clean(self):
        return self.cleaned_data

class EditarOfertaForm(forms.ModelForm):
    
    class Meta:
        model = Oferta
        fields = ['tipoOferta','nombre','imagen','descripcion','dominio','subdominio',
        'palabras_claves','lugar_aplicacion','tiempo_inicio_disponible',
        'tiempo_fin_disponible','perfil_beneficiario','perfil_cliente',
        'soluciones_alternativas','propuesta_valor','cuadro_competidores',
        'cuadro_tendencias_relevantes','estado_propiedad_intelectual','evidencia_traccion']
        labels = {
            #'nombre': _('Writer'),
        }
        help_texts = {
            #'nombre': _('Some useful help text.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("Debe escribir un nombre corto"),
            },
        }

    tipoOferta = forms.ChoiceField(
        label="Tipo de la oferta",
        choices = (
            ('1', "Emprendimiento"), 
            ('2', "Prototipo"),
            ('3', "Tecnologia")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '1',
    )

    nombre = forms.CharField(
        label="Nombre",
        max_length=150,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':'true'}
        )
    )

    descripcion = forms.CharField(
        max_length=500,
        label="Descripcion",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese una descripcion general de su oferta','rows':'4','style':'resize:none', 'required':'true'}
        )
    )

    dominio = forms.CharField(
        label="Dominio",
       # max_length=500,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':'true'}
        )
    )

    subdominio = forms.CharField(
        label="Subdominio",
        #max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':'true'}
        )
    )

    palabras_claves = forms.CharField(
        label="Palabras Claves",
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese palabras claves que se refieran a su oferta', 'required':'true'}
        )
    )

    lugar_aplicacion = forms.ChoiceField(
        label="Lugar de Aplicacion",
        choices = (
            ('1', "Azuay"),('2', "Bolivar"),('3', "Caniar"),
            ('4', "Carchi"),('5', "Chimborazo"),('6', "Cotopaxi"),('7', "El Oro"),
            ('8', "Esmeraldas"),('9', "Galapagos"),('10', "Guayas"),('11', "Imbabura"),
            ('12', "Loja"),('13', "Los Rios"),('14', "Manabi"),('15', "Morona Santiago"),
            ('16', "Napo"),('17', "Orellana"),('18', "Pastaza"),('19', "Pichincha"),
            ('20', "Santa Elena"),('21', "Santo Domingo de los Tsachilas"),('22', "Sucumbios"),('23', "Tungurahua"),('24', "Zamora Chinchipe")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':'true'}
            ),
        initial = '1',
    )

    tiempo_inicio_disponible = forms.DateField(

        label="Desde",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'true','type':'date'}
        )
    )

    tiempo_fin_disponible = forms.DateField(
        label="Hasta",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'true','type':'date'}
        )
    ) 


    perfil_beneficiario = forms.CharField(
        label="Perfil del Beneficiario",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los beneficiarios de su oferta si esta saliera al mercado','rows':'3','style':'resize:none'}
        )
    )

    perfil_cliente = forms.CharField(
        required=False,
        max_length=500,
        label="Perfil del Cliente",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los clientes de su oferta si esta saliera al mercado','rows':'3','style':'resize:none','required':'false'}
        )
    )

    soluciones_alternativas = forms.CharField(
        label="Soluciones Alternativas",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'4','style':'resize:none','required':'False'}
        )
    )

    propuesta_valor = forms.CharField(
        required=False,
        label="Propuestas de Valor",
        max_length=300,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'3','style':'resize:none','required':'false'}
        )
    )

    estado_propiedad_intelectual = forms.CharField(
        required=False,
        label="Estado Propiedad Intelectual",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'4','style':'resize:none','required':'false'}
        )
    )

    evidencia_traccion = forms.CharField(
        required=False,
        label="Evidencia de traccion",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Explique la evidencia de Traccion','rows':'4','style':'resize:none','required':'false'}
        )
    )   

    cuadroCompetidores = forms.CharField(
        label="Cuadro de Competidores",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Competidores','rows':'5','style':'resize:none','required':'false'}
        )
    )

    cuadroTendenciasRelativas = forms.CharField(
        label="Cuadro de Tendencias Relativas",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Tendencias Relativas','rows':'5','style':'resize:none','required':'false'}
        )
    )

    def clean(self):
        return self.cleaned_data

class CanvasForm(forms.ModelForm):
    
    class Meta:
        model = Oferta
        fields = [
        'redAsociados','asociacionesclave','recursosclave','propuestavalor','relacionclientes',
        'canalesDistribucion','segmentomercado','estructuracostos','fuenteingresos']
        labels = {
            #'nombre': _('Writer'),
        }
        help_texts = {
            #'nombre': _('Some useful help text.'),
        }
        error_messages = {
            'nombre': {
                'max_length': _("Debe escribir un nombre corto"),
            },
        }

    redAsociados = forms.CharField(
        label="Red de Asociados",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'13','style':'resize:none','required':'false'}
        )
    )

    asociacionesclave = forms.CharField(
        label="Actividades Clave",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )

    recursosclave = forms.CharField(
        label="Recursos Clave",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )

    propuestavalor = forms.CharField(
        label="Proposicion de Valor",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'13','style':'resize:none','required':'false'}
        )
    )

    relacionclientes = forms.CharField(
        label="Relacion con los Clientes",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )

    canalesDistribucion = forms.CharField(
        label="Canales de Distribucion",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )

    segmentomercado = forms.CharField(
        label="Segmentos de Clientes",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'13','style':'resize:none','required':'false'}
        )
    )

    estructuracostos = forms.CharField(
        label="Estructura de Costos",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )

    fuenteingresos = forms.CharField(
        label="Fuente de Ingresos",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )

    soluciones_alternativas = forms.CharField(
        required=False,
        label="Soluciones Alternativas",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'false'}
        )
    )
    
    cuadro_competidores = forms.CharField(
        required=False,
        label="Cuadro de Competidores",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Competidores','rows':'5','style':'resize:none','required':'false'}
        )
    )

    cuadro_tendencias_relevantes = forms.CharField(
        required=False,
        label="Cuadro de Tendecias Relativas",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Tendencias Relativas','rows':'5','style':'resize:none','required':'false'}
        )
    )

    def clean(self):
        return self.cleaned_data


class PorterForm(forms.ModelForm):
    
    class Meta:
        model = Oferta
        fields = ['rivalidadcompetidores','competidorespotenciales','proveedores','sustitutos','consumidores']
        labels = {
            #'nombre': _('Writer'),
        }
        help_texts = {
            #'nombre': _('Some useful help text.'),
        }
        error_messages = {
            #'nombre': {
             #   'max_length': _("Debe escribir un nombre corto"),
            #},
        }

    rivalidadcompetidores = forms.CharField(
        required=False,
        label="Rivalidad de Competidores",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa la rivalidad de los competidores del mercado','rows':'4','style':'resize:none;margin-bottom:0','required':'false'}
        )
    )

    competidorespotenciales = forms.CharField(
        required=False,
        max_length=200,
        label="Competidores Potenciales",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa si hay nuevos competidores potenciales','rows':'4','style':'resize:none;margin-bottom:0','required':'false'}
        )
    )

    proveedores = forms.CharField(
        required=False,
        label="Proveedores",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa sus proveedores','rows':'4','style':'resize:none;margin-bottom:0','required':'false'}
        )
    )

    sustitutos = forms.CharField(
        required=False,
        label="Sustitutos",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa sus productos o servicios sustitutos','rows':'4','style':'resize:none;margin-bottom:0','required':'false'}
        )
    )

    consumidores = forms.CharField(
        required=False,
        label="Consumidores",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa los consumidores de su producto','rows':'4','style':'resize:none;margin-bottom:0','required':'false'}
        )
    )

    def clean(self):
        return self.cleaned_data


class CrearDemandaForm(forms.ModelForm):
    
    class Meta:
        model = Demanda
        fields = ['tipoDemanda','nombre','imagen','descripcion','dominio','subdominio',
        'palabras_claves','lugar_aplicacion','tiempo_inicio_disponible',
        'tiempo_fin_disponible',
        'perfil_beneficiario','perfil_cliente', 
        'soluciones_alternativas','importancia_solucion']
        labels = {
            #'nombre': _('Writer'),
        }
        help_texts = {
            #'nombre': _('Some useful help text.'),
        }
        error_messages = {
            #'nombre': {
             #   'max_length': _("This writer's name is too long."),
            #},
        }

    tipoDemanda = forms.ChoiceField(
        label="Tipo de demanda",
        choices = (
            ('0', "Seleccione el tipo de demanda"), 
            ('1', "Emprendimiento"), 
            ('2', "Prototipo"),
            ('3', "Tecnologia")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )

    nombre = forms.CharField(
        label="Nombre",
        max_length=150,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su demanda', 'required':''}
        )
    )

    descripcion = forms.CharField(
        max_length=500,
        label="Descripcion",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese una descripcion general de su demanda','rows':'4','style':'resize:none', 'required':''}
        )
    )

    dominio = forms.ChoiceField(
    label="Dominio",
        choices = (
            ('0', "Mundial"), 
            ('1', "Regional"), 
            ('2', "Nivel Pais"),            
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )
    subdominio = forms.ChoiceField(
    label="Subdominio",
        choices = (
            ('0', "Todos los usuarios"), 
            ('1', "Solo usuarios de institucion"), 
            ('2', "Solo usuarios independientes"),
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )

    palabras_claves = forms.CharField(
        label="Palabras Claves",
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese palabras claves que se refieran a su demanda', 'required':''}
        )
    )

    lugar_aplicacion = forms.ChoiceField(
        label="Lugar de Aplicacion",
        choices = (
            ('0', "Seleccione la provincia"),('1', "Azuay"),('2', "Bolivar"),('3', "Caniar"),
            ('4', "Carchi"),('5', "Chimborazo"),('6', "Cotopaxi"),('7', "El Oro"),
            ('8', "Esmeraldas"),('9', "Galapagos"),('10', "Guayas"),('11', "Imbabura"),
            ('12', "Loja"),('13', "Los Rios"),('14', "Manabi"),('15', "Morona Santiago"),
            ('16', "Napo"),('17', "Orellana"),('18', "Pastaza"),('19', "Pichincha"),
            ('20', "Santa Elena"),('21', "Santo Domingo de los Tsachilas"),('22', "Sucumbios"),('23', "Tungurahua"),('24', "Zamora Chinchipe")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )

    tiempo_inicio_disponible = forms.DateField(

        label="Desde",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'','type':'date'}
        )
    )

    tiempo_fin_disponible = forms.DateField(
        label="Hasta",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'','type':'date'}
        )
    ) 

    perfil_beneficiario = forms.CharField(
        required=False,
        label="Perfil del Beneficiario",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los beneficiarios de su demanda si esta saliera al mercado','rows':'4','style':'resize:none', 'required':'False'}
        )
    )

    perfil_cliente = forms.CharField(
        required=False,
        max_length=500,
        label="Perfil del Cliente",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los clientes de su demanda si esta saliera al mercado','rows':'4','style':'resize:none','required':'False'}
        )
    )

    soluciones_alternativas = forms.CharField(
        required=False,
        label="Descripcion Alternativas",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa las alternativas','rows':'4','style':'resize:none;margin-bottom:0','required':'False'}
        )
    )
    
    importancia_solucion = forms.CharField(
        required=False,
        label="Descripcion de la Importancia",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa la descripcion de la importacia','rows':'4','style':'resize:none;margin-bottom:0','required':'False'}
        )
    )

    def clean(self):
        return self.cleaned_data
 

class EditarDemandaForm(forms.ModelForm):
    
    class Meta:
        model = Demanda
        fields = ['tipoDemanda','nombre','imagen','descripcion','dominio','subdominio',
        'palabras_claves','lugar_aplicacion','tiempo_inicio_disponible',
        'tiempo_fin_disponible',
        'perfil_beneficiario','perfil_cliente', 
        'soluciones_alternativas','importancia_solucion']
        labels = {
            #'nombre': _('Writer'),
        }
        help_texts = {
            #'nombre': _('Some useful help text.'),
        }
        error_messages = {
            #'nombre': {
             #   'max_length': _("This writer's name is too long."),
            #},
        }

    tipoDemanda = forms.ChoiceField(
        label="Tipo de demanda",
        choices = (
            ('0', "Seleccione el tipo de demanda"), 
            ('1', "Emprendimiento"), 
            ('2', "Prototipo"),
            ('3', "Tecnologia")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )

    nombre = forms.CharField(
        label="Nombre",
        max_length=150,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su demanda', 'required':''}
        )
    )

    descripcion = forms.CharField(
        max_length=500,
        label="Descripcion",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese una descripcion general de su demanda','rows':'4','style':'resize:none', 'required':''}
        )
    )

    dominio = forms.ChoiceField(
    label="Dominio",
        choices = (
            ('0', "Mundial"), 
            ('1', "Regional"), 
            ('2', "Nivel Pais"),            
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )
    subdominio = forms.ChoiceField(
    label="Subdominio",
        choices = (
            ('0', "Todos los usuarios"), 
            ('1', "Solo usuarios de institucion"), 
            ('2', "Solo usuarios independientes"),
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )

    palabras_claves = forms.CharField(
        label="Palabras Claves",
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese palabras claves que se refieran a su demanda', 'required':''}
        )
    )

    lugar_aplicacion = forms.ChoiceField(
        label="Lugar de Aplicacion",
        choices = (
            ('0', "Seleccione la provincia"),('1', "Azuay"),('2', "Bolivar"),('3', "Caniar"),
            ('4', "Carchi"),('5', "Chimborazo"),('6', "Cotopaxi"),('7', "El Oro"),
            ('8', "Esmeraldas"),('9', "Galapagos"),('10', "Guayas"),('11', "Imbabura"),
            ('12', "Loja"),('13', "Los Rios"),('14', "Manabi"),('15', "Morona Santiago"),
            ('16', "Napo"),('17', "Orellana"),('18', "Pastaza"),('19', "Pichincha"),
            ('20', "Santa Elena"),('21', "Santo Domingo de los Tsachilas"),('22', "Sucumbios"),('23', "Tungurahua"),('24', "Zamora Chinchipe")
        ),
        widget = forms.Select(
                attrs={'class':'form-group form-control infoGener', 'required':''}
            ),
        initial = '0',
    )

    tiempo_inicio_disponible = forms.DateField(

        label="Desde",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'','type':'date'}
        )
    )

    tiempo_fin_disponible = forms.DateField(
        label="Hasta",
        #initial=datetime.date.today(),
        widget=forms.DateInput(format=('%d/%m/%y'),
            attrs={'class':'form-control form-group infoGener', 'required':'','type':'date'}
        )
    ) 

    perfil_beneficiario = forms.CharField(
        required=False,
        label="Perfil del Beneficiario",
        max_length=500,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los beneficiarios de su demanda si esta saliera al mercado','rows':'4','style':'resize:none', 'required':'False'}
        )
    )

    perfil_cliente = forms.CharField(
        required=False,
        max_length=500,
        label="Perfil del Cliente",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los clientes de su demanda si esta saliera al mercado','rows':'4','style':'resize:none','required':'False'}
        )
    )

    soluciones_alternativas = forms.CharField(
        required=False,
        label="Descripcion Alternativas",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa las alternativas','rows':'4','style':'resize:none;margin-bottom:0','required':'False'}
        )
    )
    
    importancia_solucion = forms.CharField(
        required=False,
        label="Descripcion de la Importancia",
        max_length=200,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa la descripcion de la importacia','rows':'4','style':'resize:none;margin-bottom:0','required':'False'}
        )
    )

    def clean(self):
        return self.cleaned_data
