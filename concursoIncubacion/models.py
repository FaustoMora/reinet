from django.db import models
from app.models import Publicacion

# Create your models here.
class Concurso(Publicacion):
    idConcurso = models.BigIntegerField(unique=True,primary_key=True)
    idPublicacion = models.OneToOneField(Publicacion,db_column='idpublicacion',parent_link=True)
    premios = models.CharField(max_length=100)
    alcance = models.CharField(max_length=100)
    num_finalistas = models.IntegerField()
    perfil = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'detalleconcurso'
        

class Incubacion(Publicacion):
    idIncubacion = models.BigIntegerField(db_column='idDetalleIncubacion', unique=True)  # Field name made lowercase.
    idPublicacion = models.OneToOneField(Publicacion,db_column='idpublicacion',parent_link=True)
    fecha_inicio = models.DateField()
    condiciones = models.CharField(max_length=300)
    perfil_oferta = models.IntegerField()
    tipo_oferta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'detalleincubacion'


class Milestone(models.Model):
    idMilestone = models.BigIntegerField(primary_key=True)
    idPublicacion = models.ForeignKey(Publicacion, db_column='idpublicacion')
    fecha_entrega = models.DateField()
    requerimiento = models.CharField(max_length=300)
    campo_nuevo = models.CharField(max_length=300)
    peso = models.IntegerField()
    calificacion = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    relSolicitud = models.ManyToManyField('Solicitud',through="MilestoneParticipante")
    class Meta:
        managed = False
        db_table = 'milestone'


class MilestoneParticipante(models.Model):
    idMilestoneparticipante = models.BigIntegerField(primary_key=True)
    idMilestone = models.ForeignKey(Milestone, db_column='idmilestone')
    idSolicitud = models.ForeignKey('Solicitud', db_column='idsolicitud')

    class Meta:
        managed = False
        db_table = 'milestoneparticipante'
        
class Convocatoria(models.Model):
    idconvocatoria = models.BigIntegerField(unique=True, db_column='idConvocatoria') # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio') # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin') # Field name made lowercase.
    idpublicacionconvocatoria = models.ForeignKey(Publicacion, db_column='idpublicacionConvocatoria') # Field name made lowercase.
    class Meta:
        db_table = 'convocatoria'

class Solicitud(models.Model):
    idsolicitud = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey(Publicacion, db_column='idpublicacion', related_name='solicitud_publicacion')
    idofertapublicada = models.ForeignKey(Publicacion, db_column='idofertapublicada')
    fecha = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'solicitud'
