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
        fields = ['tipoOferta','nombre','descripcion','dominio','subdominio',
        'palabras_claves','lugar_aplicacion','tiempo_inicio_disponible',
        'tiempo_fin_disponible',
        'perfil_beneficiario','perfil_cliente',
        'redAsociados','asociacionesclave','recursosclave','propuestavalor','relacionclientes',
        'canalesDistribucion','segmentomercado','estructuracostos','fuenteingresos',
        'soluciones_alternativas','propuesta_valor','cuadro_competidores',
        'cuadro_tendencias_relevantes','estado_propiedad_intelectual','evidencia_traccion']
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

    tipoOferta = forms.ChoiceField(
        label="Tipo de la oferta",
        choices = (
            ('0', "Seleccione el tipo de oferta"), 
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
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':''}
        )
    )

    descripcion = forms.CharField(
        max_length=500,
        label="Descripcion",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese una descripcion general de su oferta','rows':'4','style':'resize:none', 'required':''}
        )
    )

    dominio = forms.CharField(
        label="Dominio",
        max_length=500,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':''}
        )
    )

    subdominio = forms.CharField(
        label="Subdominio",
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese el nombre de su oferta', 'required':''}
        )
    )

    palabras_claves = forms.CharField(
        label="Palabras Claves",
        max_length=200,
        widget=forms.TextInput(
            attrs={'class':'form-control form-group infoGener', 'placeholder':'Ingrese palabras claves que se refieran a su oferta', 'required':''}
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
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los beneficiarios de su oferta si esta saliera al mercado','rows':'4','style':'resize:none', 'required':'False'}
        )
    )

    perfil_cliente = forms.CharField(
        required=False,
        label="Perfil del Cliente",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el perfil de los clientes de su oferta si esta saliera al mercado','rows':'4','style':'resize:none','required':'False'}
        )
    )

    redAsociados = forms.CharField(
        label="Red de Asociados",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'13','style':'resize:none','required':'False'}
        )
    )

    asociacionesclave = forms.CharField(
        label="Actividades Clave",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    recursosclave = forms.CharField(
        label="Recursos Clave",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    propuestavalor = forms.CharField(
        label="Proposicion de Valor",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'13','style':'resize:none','required':'False'}
        )
    )

    relacionclientes = forms.CharField(
        label="Relacion con los Clientes",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none'}
        )
    )

    canalesDistribucion = forms.CharField(
        label="Canales de Distribucion",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    segmentomercado = forms.CharField(
        label="Segmentos de Clientes",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'13','style':'resize:none','required':'False'}
        )
    )

    estructuracostos = forms.CharField(
        label="Estructura de Costos",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    fuenteingresos = forms.CharField(
        label="Fuente de Ingresos",
        required=False,
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )





    soluciones_alternativas = forms.CharField(
        required=False,
        label="Soluciones Alternativas",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    propuesta_valor = forms.CharField(
        required=False,
        label="Propuestas de Valor",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    estado_propiedad_intelectual = forms.CharField(
        required=False,
        label="Estado Propiedad Intelectual",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Escriba aqui','rows':'5','style':'resize:none','required':'False'}
        )
    )

    evidencia_traccion = forms.CharField(
        required=False,
        label="Evidencia de traccion",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Explique la evidencia de Traccion','rows':'5','style':'resize:none','required':'False'}
        )
    )

    cuadro_competidores = forms.CharField(
        required=False,
        label="Cuadro de Competidores",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Competidores','rows':'5','style':'resize:none','required':'False'}
        )
    )

    cuadro_tendencias_relevantes = forms.CharField(
        required=False,
        label="Cuadro de Tendecias Relativas",
        widget = forms.Textarea(
            attrs={'class':'form-control form-group',
            'placeholder':'Describa el cuadro de Tendencias Relativas','rows':'5','style':'resize:none','required':'False'}
        )
    )


    def clean(self):
        return self.cleaned_data