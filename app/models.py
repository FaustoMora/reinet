"""
Definition of models.
"""

from django.db import models
from usuarios.models import Persona
from django.contrib.auth.models import User
# Create your models here. DE LA APP

class Catalogo(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idCatalogo")
    codigo = models.CharField(max_length=30,blank=True, db_column="codigoCatalogo")
    descripcion = models.CharField(max_length=100L, blank=True,db_column="descripcionCatalogo")
    padre = models.ForeignKey('self', null=True, db_column='idcatalogopadre',related_name="hijos")
    class Meta:
        db_table = 'Catalogo'
"""
class Comentario(models.Model):
    idcomentario = models.BigIntegerField(unique=True)
    idusuario = models.ForeignKey('Persona', db_column='idusuario')
    comentario = models.CharField(max_length=500L)
    calificacion = models.IntegerField(null=True, blank=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    class Meta:
        db_table = 'comentario'
"""
class Publicacion(models.Model):
    idpublicacion = models.AutoField(unique=True,primary_key=True)
    idusuario = models.ForeignKey(User, db_column='idusuario')
    nombre = models.CharField(max_length=150L)
    descripcion = models.CharField(max_length=500L)
    dominio = models.CharField(max_length=200L)
    subdominio = models.CharField(max_length=200L)
    class Meta:
        db_table = 'publicacion'

