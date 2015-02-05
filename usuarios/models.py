# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from app.models import *


"""
class Equipo(models.Model):
    idequipo = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    idusuario = models.ForeignKey('Persona', db_column='id')
    rol = models.CharField(max_length=100L)
    class Meta:
        db_table = 'equipo'
"""
"""
class Imagen(models.Model):
    idimagen = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    enlace_imagen = models.CharField(max_length=100L)
    class Meta:
        db_table = 'imagen'
"""
class Institucion(User):
    idinstitucion = models.AutoField(primary_key=True)
    nombre_corto = models.CharField(max_length=20L)
    descripcion = models.CharField(max_length=900L)
    mision = models.CharField(max_length=900L)
    sitio_web = models.CharField(max_length=200L)
    persona_que_registra = models.CharField(max_length=200L)
    idadministrador = models.IntegerField(db_column='idAdministrador') # Field name made lowercase.
    telefono = models.CharField(max_length=15L)
    recursos = models.CharField(max_length=100L)
    miembros = models.ManyToManyField('Persona', through='InstitucionPersona')

    class Meta:
        db_table = 'institucion'


class InstitucionPersona(models.Model):
    idpersona = models.ForeignKey('Persona', db_column='idpersona')
    idinstitucion = models.ForeignKey(Institucion, db_column='idinstitucion')
    cargoPersona = models.CharField(max_length=50, )
    class Meta:
        db_table = 'institucion_persona'


class Persona(User):
    idpersona = models.AutoField(primary_key=True)
    identificacion = models.CharField(max_length=20L)
    cargo = models.CharField(max_length=50L)
    actividad = models.CharField(max_length=150L)
    fecha_nacimiento = models.DateField()
    areas_interes = models.CharField(max_length=50L)
    #idusuario = models.ForeignKey(AuthUser, db_column='id')
    class Meta:
        db_table = 'persona'

class Mensaje(models.Model):
    idEmisor=models.ForeignKey(Persona,db_column='idpersEmisor', related_name='p_emisor')
    idDestimo=models.ForeignKey(Persona,db_column='idpersDest', related_name='p_destino')
    txtMensaje=models.CharField(max_length=250)
    fecha=models.DateField()
    hora=models.TimeField()
    class Meta:
        db_table = 'mensaje'
"""
class Politicaprivacidad(models.Model):
    idusuario = models.ForeignKey('Persona', db_column='idusuario')
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    tipo_alcance = models.CharField(max_length=50L)
    class Meta:
        db_table = 'politicaprivacidad'
"""