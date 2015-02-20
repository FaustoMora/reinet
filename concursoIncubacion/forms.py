'''
Created on 11/2/2015

@author: Dark Legion
'''
from django import forms
from app.models import *
from models import *
from usuarios.models import Persona

class CrearConcursoForm(forms.ModelForm):
	
	class Meta:

		model = Concurso
		fields = ['nombre','descripcion','fecha_inicio','fecha_fin','dominio','subdominio','alcance','perfil','tipo_oferta','num_finalistas','premios', 'imagen']


	TiposOfertaChoice = (('1','Tecnologia'),('2','Emprendimiento'),('3','Prototipo'))

	nombre = forms.CharField(label="Nombre",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese el nombre del Concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	descripcion = forms.CharField(label="Descripcion",widget=forms.Textarea(attrs={'rows':4, 'cols':60,'class':'form-control', 'placeholder':'Ingrese una breve descripcion del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	#condiciones = forms.CharField(label="Condiciones",widget=forms.Textarea(attrs={'rows':3, 'cols':60, 'class':'form-control', 'placeholder':'Ingrese las condiciones del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	fecha_inicio = forms.DateField(label="Fecha Inicio",widget=forms.DateInput(format=('%d/%m/%y'),attrs={'class':'form-control','placeholder':'Fecha inicio de concurso (m/d/Y)','required':''}))
	fecha_fin = forms.DateField(label="Fecha Final",widget=forms.DateInput(format=('%d/%m/%y'),attrs={'class':'form-control','placeholder':'Fecha fin de concurso (m/d/Y)','required':''}))
	dominio = forms.CharField(label="Dominio",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Describa el dominio del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	subdominio = forms.CharField(label="Sub-Dominio",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Describa el sub-dominio del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	alcance = forms.CharField(label="Alcance",widget=forms.Textarea(attrs={'rows':3, 'cols':60, 'class':'form-control', 'placeholder':'Describa el alcance del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	perfil = forms.CharField(label="Perfil",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Describa el perfil de las ofertas que se buscan','data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	tipo_oferta=forms.ChoiceField(label="Tipo Oferta",choices=TiposOfertaChoice,widget=forms.Select(attrs={'class':'form-control','data-toggle':'popover','placeholder':'Elija el tipo de oferta para el concurso', 'required':''}))
	num_finalistas=forms.IntegerField(label="Numero de Finalistas",widget=forms.TextInput(attrs={'type':'number','class':'form-control','data-placement':'left','placeholder':'Ingrese la cantidad de finalistas permitidos','data-toggle':'popover', 'required':''}))
	premios = forms.CharField(label="Premios",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Describa el premio final del concurso','data-trigger':'focus','data-placement':'left','data-toggle':'popover'}))
	imagen = forms.ImageField(label="Cargar Imagen",widget=forms.FileInput(attrs={'class':'btn btn-default','data-trigger':'focus','data-placement':'left','data-toggle':'popover'}))

	def clean(self):
		return self.cleaned_data
                
