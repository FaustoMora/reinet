from django.db import models
from usuarios.models import Persona
from django.contrib.auth.models import User
from app.models import Publicacion

# Create your models here.
class Concurso(models.Model):
	idConcurso = models.AutoField(db_column='idConcurso',unique=True,primary_key=True)
	idusuario = models.ForeignKey(User, db_column='idusuario')
	nombre = models.CharField(max_length=150L)
	descripcion = models.CharField(max_length=500L)
	dominio = models.CharField(max_length=200L)
	subdominio = models.CharField(max_length=200L)
	fecha_inicio=models.DateField(db_column='fechaInicio')
	fecha_fin=models.DateField(db_column='fechaFin')
	premios = models.CharField(max_length=200)
	alcance = models.CharField(max_length=300)
	num_finalistas = models.IntegerField()
	perfil = models.CharField(max_length=200)
	tipo_oferta = models.IntegerField()
	estado = models.IntegerField()
	imagen = models.ImageField(upload_to='conInc_media')

	def __unicode__(self):
		return self.image.name

	class Meta:
		db_table = 'concursos'
        

class Incubacion(models.Model):
    idIncubacion = models.AutoField(db_column='idDetalleIncubacion', unique=True,primary_key=True)  # Field name made lowercase.
    idusuario = models.ForeignKey(User, db_column='idusuario')
    nombre = models.CharField(max_length=150L)
    descripcion = models.CharField(max_length=500L)
    dominio = models.CharField(max_length=200L)
    subdominio = models.CharField(max_length=200L)
    fecha_inicio=models.DateField(db_column='fechaInicio')
    condiciones = models.CharField(max_length=300)
    perfil_oferta = models.CharField(max_length=200)
    tipo_oferta = models.IntegerField()
    estado = models.IntegerField()
    imagen = models.ImageField(upload_to='conInc_media')

    def __unicode__(self):
        return self.image.name

    class Meta:
        db_table = 'incubacion'


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
