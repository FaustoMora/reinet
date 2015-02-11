'''
Created on 11/2/2015

@author: Dark Legion
'''
from django import forms
from app.models import *
from models import *
from usuarios.models import Persona

class crearConcursoForm(forms.Form):
    TiposOfertaChoice = (('1','Tecnologia'),('2','Emprendimiento'),('3','Prototipo'))

    nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Ingrese el nombre del Concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    descripcion = forms.CharField(label="Descripcion",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Ingrese una breve descripcion del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    condiciones = forms.CharField(label="Condiciones",widget=forms.TextInput(attrs={'class':'form-group  form-control', 'placeholder':'Ingrese las condiciones del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    fechainicio = forms.DateField(label="Fecha Inicio",widget=forms.DateInput(format=('%d/%m/%y'),attrs={'class':'form-group col-xs-6 form-control','placeholder':'Fecha inicio de concurso (d/m/Y)','required':''}))
    fechafin = forms.DateField(label="Fecha Final",widget=forms.DateInput(format=('%d/%m/%y'),attrs={'class':'form-group col-xs-6 form-control','placeholder':'Fecha fin de concurso (d/m/Y)','required':''}))
    dominio = forms.CharField(label="Dominio",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Describa el dominio del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    subdominio = forms.CharField(label="Sub-Dominio",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Describa el sub-dominio del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    alcance = forms.CharField(label="Alcance",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Describa el alcance del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    perfil = forms.CharField(label="Perfil",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Describa el perfil de las ofertas que se buscan','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
    tipooferta=forms.ChoiceField(label="Tipo Oferta",choices=TiposOfertaChoice,widget=forms.Select(attrs={'class':'form-control','data-toggle':'popover','placeholder':'Elija el tipo de oferta para el concurso', 'required':''}))
    #diriguido=
    #jurado=
    #consultores=
    numfinalistas=forms.IntegerField(label="Numero de Finalistas",widget=forms.TextInput(attrs={'type':'number','class':'form-group form-control','data-placement':'left','placeholder':'Ingrese la cantidad de finalistas permitidos','data-toggle':'popover', 'required':''}))
    premios = forms.CharField(label="Premios",widget=forms.TextInput(attrs={'class':'form-group form-control', 'placeholder':'Describa el premio final del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover'}))

    def clean(self):
        return self.cleaned_data
                
