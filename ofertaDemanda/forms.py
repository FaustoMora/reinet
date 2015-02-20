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




class CrearOfertaForm(forms.ModelForm):
	
    class Meta:

        model = Oferta
        fields = ['nombre','descripcion','palabras_claves','tiempo_inicio_disponible','tiempo_fin_disponible','lugar_aplicacion','perfil_beneficiario','perfil_cliente','soluciones_alternativas','propuesta_valor','cuadro_competidores','cuadro_tendencias_relevantes','imagen','estado_propiedad_intelectual']


    TiposOfertaChoice = (('1','Tecnologia'),('2','Emprendimiento'),('3','Prototipo'))

    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre de la oferta','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    descripcion = forms.CharField(label="Descripcion",widget=forms.Textarea(attrs={'rows':4, 'cols':60,'class':'form-control', 'placeholder':'Ingrese una breve descripcion de la oferta','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    palabras_claves = forms.CharField(label="Palabras Clave",widget=forms.Textarea(attrs={'rows':4, 'cols':60,'class':'form-control', 'placeholder':'Ingrese palabras clave de la oferta','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    tiempo_inicio_disponible = forms.DateField(label="Fecha Inicio",widget=forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','placeholder':'Fecha inicial de la oferta (m/d/Y)','required':''}))
    tiempo_fin_disponible = forms.DateField(label="Fecha Final",widget=forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control','placeholder':'Fecha fin de la oferta (m/d/Y)','required':''}))
    lugar_aplicacion = forms.CharField(label="Lugar",widget=forms.Textarea(attrs={'rows':4, 'cols':60,'class':'form-control', 'placeholder':'Ingrese el lugar','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    perfil_beneficiario = forms.CharField(label="Perfil del beneficiario de la oferta",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el beneficiario de la oferta','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    perfil_cliente = forms.CharField(label="Perfil del cliente de la oferta",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el cliente de la oferta','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    soluciones_alternativas = forms.CharField(label="Descripcion de soluciones alternativas existentes",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el cliente de la oferta','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    propuesta_valor = forms.CharField(label="Descripcion de la propuesta por valor",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'ingrese la descripcion','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    cuadro_competidores = forms.CharField(label="Business model canvas",widget=forms.Textarea(attrs={'rows':3, 'cols':60, 'class':'form-control', 'placeholder':'Ingrese el business model canvas','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    cuadro_tendencias_relevantes = forms.CharField(label="Diagrama de Porter",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Diagrama de porter','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    imagen = forms.ImageField(label="Cargar Imagen",widget=forms.FileInput(attrs={'class':'btn btn-default','data-trigger':'focus','data-placement':'left','data-toggle':'popover'}))  
    estado_propiedad_intelectual = forms.CharField(label="Estado de la propiedad intelectual",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el estado de la propiedad intelectual','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	

    def clean(self):
        return self.cleaned_data
                
