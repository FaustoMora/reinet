from django.db import models
from usuarios.models import *

# Create your models here.


class Convocatoria(models.Model):
    idconvocatoria = models.BigIntegerField(unique=True, db_column='idConvocatoria') # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio') # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin') # Field name made lowercase.
    idpublicacionconvocatoria = models.ForeignKey('Publicacion', db_column='idpublicacionConvocatoria') # Field name made lowercase.
    class Meta:
        db_table = 'convocatoria'

class Detalleconcurso(models.Model):
    iddetalleconcurso = models.BigIntegerField(unique=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    premios = models.CharField(max_length=100L)
    alcance = models.CharField(max_length=100L)
    num_finalistas = models.IntegerField()
    perfil = models.CharField(max_length=100L)
    estado = models.CharField(max_length=30L)
    class Meta:
        db_table = 'detalleconcurso'

class Detalleincubacion(models.Model):
    iddetalleincubacion = models.BigIntegerField(unique=True, db_column='idDetalleIncubacion') # Field name made lowercase.
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    fecha_inicio = models.DateField()
    condiciones = models.CharField(max_length=300L)
    perfil_oferta = models.IntegerField()
    tipo_oferta = models.IntegerField()
    class Meta:
        db_table = 'detalleincubacion'

class Milestone(models.Model):
    idmilestone = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    fecha_entrega = models.DateField()
    requerimiento = models.CharField(max_length=300L)
    campo_nuevo = models.CharField(max_length=300L)
    peso = models.IntegerField()
    calificacion = models.IntegerField(null=True, blank=True)
    estado = models.IntegerField()
    class Meta:
        db_table = 'milestone'

class Milestoneparticipante(models.Model):
    idmilestoneparticipante = models.BigIntegerField(primary_key=True)
    idmilestone = models.ForeignKey(Milestone, db_column='idmilestone')
    idsolicitud = models.ForeignKey('Solicitud', db_column='idsolicitud')
    class Meta:
        db_table = 'milestoneparticipante'

class Publicacion(models.Model):
    idpublicacion = models.BigIntegerField(unique=True)
    #idusuario = models.ForeignKey('Persona', db_column='idpersona')
    nombre = models.CharField(max_length=150L)
    descripcion = models.CharField(max_length=500L)
    dominio = models.IntegerField()
    subdominio = models.IntegerField()
    class Meta:
        db_table = 'publicacion'

class Solicitud(models.Model):
    idsolicitud = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey(Publicacion, db_column='idpublicacion', related_name='solicitud_publicacion')
    idofertapublicada = models.ForeignKey(Publicacion, db_column='idofertapublicada')
    fecha = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'solicitud'

