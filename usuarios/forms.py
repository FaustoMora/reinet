"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
	email=forms.EmailField(required=True)
	Nacimiento=forms.DateField(required=False)
	
	class Meta:
		model= User
		fields=('username', 'email','Nacimiento', 'password1', 'password2')
	
	def save(self, commit=True):
		user=super(UserCreationForm, self).save(commit=False)
		user.email=self.cleaned_data['email']
		
		if commit:
			user.save()
			
		return user

"""
from django import forms
from models import  AuthUser, Persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

"""
class UsuarioForm(forms.ModelForm):
	
	class Meta:
		model=Usuario
		fields=['nombre', 'password']
		widgets = {
		 'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}),
		 'password': forms.TextInput(attrs={'class': 'form-control'}),
				
"""

class UsuarioForm2(UserCreationForm):
	nombre=forms.CharField(label="Nombre", 
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre', 'data-content':'Ingresa un nombre'
			,'data-trigger':'focus','data-placement':'left','data-toggle':'popover', 'required':''}))
	apellidos=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellidos', 'required':''}))
	email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email', 'type':'email'
		, 'required':''}))
	identificacion=forms.CharField(	widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Identificacion', 'required':''}))
	cargo=forms.CharField(label="Cargo",
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cargo', 'required':''}))
	actividad=forms.CharField(label="Actividad que realiza",
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Actividad que realiza'}))
	sitioweb=forms.CharField(label="URL de su sitio web",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Sitio web', 'required':''}))
	ciudad=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad', 'required':''}))
	#fechaNac=forms.DateField(label="Fecha de Nacimiento", widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Fecha de Nacimiento', 'required':''}))
	areasInt=forms.CharField(label="Areas de Interes",
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Areas de Interes'}))
	#password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control margin-bottom-xs', 
		#'placeholder':'Password', 'required':''}))

	class Meta:
		model=User
		fields=['username','password1', 'password2']

		widgets = {
			'password1': forms.PasswordInput(attrs={'class':'form-control margin-bottom-xs', 'placeholder':'Password'}),
			'password2': forms.PasswordInput(attrs={'class':'form-control margin-bottom-xs','placeholder':'Confirma Password'}),
			'username':forms.TextInput(attrs={'class':'form-control margin-bottom-xs'})
			}


	def save(self, commit=True):
		user=super(UsuarioForm2, self).save(commit=False)
		user.email=self.cleaned_data['email']
		
		if commit:
			user.save()
			p=Persona()
			p.nombre=self.cleaned_data['nombre']
			p.idPersona='default'
			p.email=self.cleaned_data['email']
			p.identificacion=self.cleaned_data['identificacion']
			p.sitioweb=self.cleaned_data['sitioweb']
			p.fecha_nacimiento='2012-12-12'
			p.areas_interes=self.cleaned_data['areasInt']
			p.actividad=self.cleaned_data['actividad']
			p.cargo=self.cleaned_data['cargo']
			p.idUsuario='null';
			p.save()
			
		
		
		return user
