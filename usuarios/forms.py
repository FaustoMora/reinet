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
			p.user_id=user.id
			p.save()
			
		
		
		return user

class PersonaForm(UserCreationForm):

	class Meta:
		model=Persona
		exclude=['last_login','is_superuser','user_permissions','is_staff','groups'
		,'date_joined','idpersona','is_active','fecha_nacimiento','password']
		fields=['username','first_name','last_name', 'email','identificacion',
		'cargo','actividad','areas_interes','password1','password2']
		widgets={
			'password': forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}),
			
			'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
			
			'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}),
			
			'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellidos'}),
			
			'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}),
			
			'identificacion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Identificacion'}),
			
			'cargo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cargo'}),
			
			'actividad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Actividad'}),

			'areas_interes': forms.TextInput(attrs={'class': 'form-control','placeholder':'Areas de Interes'}),

			'password1': forms.TextInput(attrs={'class': 'form-control','placeholder':'Password'}),
			
		}
	#imagen = forms.ImageField(label="Imagen Perfil",widget=forms.FileInput(attrs={'class':'btn btn-default','data-trigger':'focus','data-placement':'left','data-toggle':'popover'}))

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
			
			'identificacion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Identificacion'}),
			
			'cargo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cargo'}),
			
			'actividad': forms.TextInput(attrs={'class': 'form-control','placeholder':'Actividad'}),

			'areas_interes': forms.TextInput(attrs={'class': 'form-control','placeholder':'Areas de Interes'}),

		}

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
	recibe=forms.CharField(label='Para')
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