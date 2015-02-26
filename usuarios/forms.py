# -*- encoding: utf-8 -*-
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
from models import  *
from django.contrib.auth.forms import *
from django.contrib.auth.models import User
from datetime import datetime
#from phonenumber_field.modelfields import PhoneNumberField
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
			'password1': forms.PasswordInput(attrs={'class':'form-control margin-bottom-xs', 'placeholder':'Contraseña'}),
			'password2': forms.PasswordInput(attrs={'class':'form-control margin-bottom-xs','placeholder':'Confirmar Contraseña'}),
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
			p.user_id=user.id
			p.save()
			
		
		
		return user

class PersonaForm(UserCreationForm):

	class Meta:
		model=Persona
		exclude=['last_login','is_superuser','user_permissions','is_staff','groups'
		,'date_joined','idpersona','is_active','fecha_nacimiento','password']

		fields=['username','first_name','last_name', 'email','imagen','identificacion',
		'cargo','actividad','areas_interes','password1','password2']
		widgets={
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Contraseña'}),
			
			'cargo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cargo'}),
			
			'actividad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Actividad'}),

			'areas_interes': forms.TextInput(attrs={'class': 'form-control','placeholder':'Areas de Interés'}),

			'password1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Password'}),
			
		}
	username=forms.CharField(label='Usuario',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
	first_name=forms.CharField(label='Nombres',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}))
	last_name=forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellidos'}))
	email=forms.EmailField(label='Correo Electrónico',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su dirección de Correo electrónico'}))	
	identificacion=forms.CharField(label='Identificación',widget=forms.TextInput(attrs={'class': 'form-control','pattern':"[0-9]{1,15}",'placeholder':'Número de cédula o pasaporte'}))	
	password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirmacion'}))
	password2=forms.CharField(label='Confirmación de Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirmacion'}))
	imagen = forms.ImageField(label="Imagen de Perfil",widget=forms.FileInput())

	def save(self, commit=True):
		user=super(PersonaForm, self).save(commit=False)
		#user.idpersona='default'
		user.fecha_nacimiento='2012-12-12'
		if commit:
			user.save()
			
		return user

class PersonaEditarForm(forms.ModelForm):

	class Meta:
		model=Persona
		#exclude=['last_login','is_superuser','user_permissions','is_staff','groups'
		#,'date_joined','idpersona','is_active','fecha_nacimiento','password','username','password1', 'password2']
		fields=['first_name','last_name','email','identificacion','cargo','actividad','areas_interes','imagen']
		
		widgets={
			
			'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}),
			
			'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellidos'}),
			
			'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
			
			'identificacion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Identificación'}),
			
			'cargo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cargo'}),
			
			'actividad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Actividad'}),

			'areas_interes': forms.TextInput(attrs={'class': 'form-control','placeholder':'Areas de Interés'}),

		}

	first_name=forms.CharField(label='Nombres',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}))
	last_name=forms.CharField(label='Apellidos',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellidos'}))
	email=forms.EmailField(label='Correo Electrónico',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su dirección de Correo electrónico'}))	
	identificacion=forms.CharField(label='Identificación',widget=forms.TextInput(attrs={'class': 'form-control','pattern':"[0-9]{1,15}",'placeholder':'Número de cédula o pasaporte'}))	
	

	def clean(self):
		return self.cleaned_data
	"""
	def save(self, commit=True):
		#user=super(PersonaForm, self).save(commit=False)
		#user.idpersona='default'
		user.fecha_nacimiento='2012-12-12'
		if commit:
			user.save()
			
		return user
		"""
class MensajeForm(forms.ModelForm):
	recibe=forms.CharField(label='Para', widget= forms.TextInput(attrs={'class': 'form-control','placeholder':'Destinatario'}))
	txtMensaje=forms.CharField(label='Mensaje',widget=forms.Textarea(attrs={'class': 'form-control'}))
	asunto=forms.CharField(label='Asunto',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Asunto'}))
	class Meta:
		model=Mensaje
		fields=['recibe','asunto','txtMensaje']
		"""
		def save(self, commit=True):
			#mensaje=super(MensajeForm,self).save(commit=False)
			#mensaje.idEmisor=1
			mensaje.fecha='2012-12-12'
			mensaje.hora=null
			p=Persona.objects.get(username=recibe)
			print "persooona", p
			mensaje.idDestino=p.idpersona
			#if commit:
				#mensaje.save()
			return mensaje
		"""
class ImagenPerfilForm(forms.ModelForm):
	class Meta:
		model=Persona
		fields=['imagen']




class InstitucionForm(UserCreationForm):

	class Meta:
		model=Institucion
		exclude=['last_login','is_superuser','user_permissions','is_staff','groups'
		,'date_joined','idinstitucion' ,'is_active','password','last_name']

		fields=['username','first_name','nombre_corto','descripcion','mision','sitio_web',
		'persona_que_registra','email','telefono','recursos','imagen','password1','password2']

	username=forms.CharField(label='Usuario Institución',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}))
	first_name=forms.CharField(max_length=50,label='Nombre de la Institución',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el nombre completo de su Institución'}))
	nombre_corto=forms.CharField(label='Abreviatura',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre abreviado de la Institución'}))
	descripcion = forms.CharField(label='Descripción',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese una breve descripcion de la Institución'}))
	mision = forms.CharField(label='Misión',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Describa la Misión de su Institución'}))
	sitio_web = forms.CharField(label='Sitio Web',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'URL del Sitio Web de su Institución'}))	
	telefono = forms.CharField(label='Teléfono',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el número de teléfono de la Institución'}))
	recursos = forms.CharField(label='Recursos',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Recursos de la Institución'}))	
	persona_que_registra=forms.CharField(label='Administrador de Institución',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del Usuario que administrará la Institución'}))
	email=forms.CharField(label='Email de Administrador',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Dirección Email del Administrador de la Institución'}))
	password2=forms.CharField(label='Confirmación de Contraseña',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Confirmación'}))
	#imagen = forms.ImageField(label="Imagen Perfil",widget=forms.FileInput(attrs={'class':'btn btn-default','data-trigger':'focus','data-placement':'left','data-toggle':'popover'}))

	def save(self, commit=True):
		user1=super(InstitucionForm, self).save(commit=False)
		#user.idpersona='default'		
		if commit:
			user1.save()
			
		return user1


class InstitucionEditarForm(forms.ModelForm):

	class Meta:
		model=Institucion
		#exclude=['last_login','is_superuser','user_permissions','is_staff','groups'
		#,'date_joined','idpersona','is_active','fecha_nacimiento','password','username','password1', 'password2']
		fields=['first_name','nombre_corto','descripcion','mision','sitio_web',
		'email','telefono','recursos','imagen']
		
	first_name=forms.CharField(max_length=50,label='Nombre de la Institución',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el nombre completo de su Institución'}))
	nombre_corto=forms.CharField(label='Abreviatura',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre abreviado de la Institución'}))
	descripcion = forms.CharField(label='Descripción',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese una breve descripcion de la Institución'}))
	mision = forms.CharField(label='Misión',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Describa la Misión de su Institución'}))
	sitio_web = forms.CharField(label='Sitio Web',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'URL del Sitio Web de su Institución'}))	
	telefono = forms.CharField(label='Teléfono',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el número de teléfono de la Institución'}))
	recursos = forms.CharField(label='Recursos',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Recursos de la Institución'}))	
	email=forms.CharField(label='Email de Administrador',widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre del Usuario que administrará la Institución'}))


	def clean(self):
		return self.cleaned_data
	"""
	def save(self, commit=True):
		#user=super(PersonaForm, self).save(commit=False)
		#user.idpersona='default'
		user.fecha_nacimiento='2012-12-12'
		if commit:
			user.save()
			
		return user
		"""