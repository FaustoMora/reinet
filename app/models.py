"""
Definition of models.
"""

from django.db import models
from usuarios.models import Persona
from django.contrib.auth.models import User

# Create your models here. DE LA APP
"""
class Catalogo(models.Model):
    idcatalogo = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=10L, blank=True)
    descripcion = models.CharField(max_length=100L, blank=True)
    idcatalogopadre = models.ForeignKey('self', null=True, db_column='idcatalogopadre', blank=True)
    class Meta:
        db_table = 'catalogo'

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
    idpublicacion = models.BigIntegerField(unique=True)
    idusuario = models.ForeignKey(User, db_column='idusuario')
    nombre = models.CharField(max_length=150L)
    descripcion = models.CharField(max_length=500L)
    dominio = models.IntegerField()
    subdominio = models.IntegerField()
    class Meta:
        db_table = 'publicacion'


