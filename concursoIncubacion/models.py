from django.db import models
from app.models import Publicacion

# Create your models here.
class Concurso(Publicacion):
    idConcurso = models.AutoField(db_column='idDetalleConcurso',unique=True,primary_key=True)
    idPublicacion = models.OneToOneField(Publicacion,db_column='idpublicacion',parent_link=True)
    fecha_inicio=models.DateField(db_column='fechaInicio')
    fecha_fin=models.DateField(db_column='fechaFin')
    premios = models.CharField(max_length=200)
    alcance = models.CharField(max_length=300)
    num_finalistas = models.IntegerField()
    perfil = models.CharField(max_length=200)
    tipo_oferta = models.IntegerField()
    estado = models.IntegerField()

    class Meta:
        db_table = 'detalleconcurso'
        

class Incubacion(Publicacion):
    idIncubacion = models.AutoField(db_column='idDetalleIncubacion', unique=True,primary_key=True)  # Field name made lowercase.
    idPublicacion = models.OneToOneField(Publicacion,db_column='idpublicacion',parent_link=True)
    fecha_inicio = models.DateField()
    condiciones = models.CharField(max_length=300)
    perfil_oferta = models.IntegerField()
    tipo_oferta = models.IntegerField()

    class Meta:
        db_table = 'detalleincubacion'


class Solicitud(models.Model):
    idsolicitud = models.AutoField(primary_key=True)
    idpublicacion = models.ForeignKey(Publicacion, db_column='idpublicacion', related_name='solicitud_publicacion')
    idofertapublicada = models.ForeignKey(Publicacion, db_column='idofertapublicada')
    fecha = models.DateField(db_column='fechaSol')

    class Meta:
        db_table = 'solicitud'


class Milestone(models.Model):
    idMilestone = models.AutoField(primary_key=True)
    idPublicacion = models.ForeignKey(Publicacion, db_column='idpublicacion')
    fecha_entrega = models.DateField()
    requerimiento = models.CharField(max_length=300)
    campo_nuevo = models.CharField(max_length=300)
    peso = models.IntegerField()
    calificacion = models.IntegerField(blank=True, null=True)
    estado = models.IntegerField()
    relSolicitud = models.ManyToManyField(Solicitud,through="MilestoneParticipante")

    class Meta:
        db_table = 'milestone'


class MilestoneParticipante(models.Model):
    idMilestoneparticipante = models.AutoField(primary_key=True)
    idMilestone = models.ForeignKey(Milestone, db_column='idmilestone')
    idSolicitud = models.ForeignKey(Solicitud, db_column='idsolicitud')

    class Meta:
        db_table = 'milestoneparticipante'

        
class Convocatoria(models.Model):
    idconvocatoria = models.AutoField( db_column='idConvocatoria',unique=True,primary_key=True) # Field name made lowercase.
    fechainicio = models.DateField(db_column='fechaInicio') # Field name made lowercase.
    fechafin = models.DateField(db_column='fechaFin') # Field name made lowercase.
    idpublicacionconvocatoria = models.ForeignKey(Publicacion, db_column='idpublicacionConvocatoria') # Field name made lowercase.

    class Meta:
        db_table = 'convocatoria'
