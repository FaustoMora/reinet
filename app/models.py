"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Catalogo(models.Model):
    idcatalogo = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=10, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    idcatalogopadre = models.ForeignKey('self', db_column='idcatalogopadre', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogo'
        
        
        
class Comentario(models.Model):
    idcomentario = models.BigIntegerField(unique=True)
    idusuario = models.ForeignKey('Usuario', db_column='idusuario')
    comentario = models.CharField(max_length=500)
    calificacion = models.IntegerField(blank=True, null=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')

    class Meta:
        managed = False
        db_table = 'comentario'
        
        

class Convocatoria(models.Model):
    idconvocatoria = models.BigIntegerField(db_column='idConvocatoria', unique=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio')  # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin')  # Field name made lowercase.
    idpublicacionconvocatoria = models.ForeignKey('Publicacion', db_column='idpublicacionConvocatoria')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'convocatoria'
        

class Equipo(models.Model):
    idequipo = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    idusuario = models.ForeignKey('Usuario', db_column='idusuario')
    rol = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'equipo'


class Imagen(models.Model):
    idimagen = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    enlace_imagen = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'imagen'
        
        
class Publicacion(models.Model):
    idpublicacion = models.BigIntegerField(unique=True)
    idusuario = models.ForeignKey('Usuario', db_column='idusuario')
    nombre = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    dominio = models.IntegerField()
    subdominio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'publicacion'

