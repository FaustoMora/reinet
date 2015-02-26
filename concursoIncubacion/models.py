from django.db import models
from usuarios.models import *
from django.contrib.auth.models import User
from ofertaDemanda.models import Oferta
from app.models import Catalogo

# Create your models here.
class Concurso(models.Model):
    idConcurso = models.AutoField(db_column='idConcurso',unique=True,primary_key=True)
    idusuario = models.ForeignKey(User, db_column='idusuario')
    nombre = models.CharField(max_length=150L)
    descripcion = models.TextField()
    condiciones = models.TextField()
    dominio = models.CharField(max_length=200L)
    subdominio = models.CharField(max_length=200L)
    fecha_inicio=models.DateField(db_column='fechaInicio')
    fecha_fin=models.DateField(db_column='fechaFin')
    premios = models.TextField()
    alcance = models.TextField()
    num_finalistas = models.PositiveIntegerField()
    perfil = models.CharField(max_length=200)
    tipo_oferta = models.IntegerField()
    estado = models.ForeignKey(Catalogo, db_column="estado")
    imagen = models.ImageField(upload_to='conInc_media')
    ranking = models.IntegerField()

    def __unicode__(self):
        return self.image.name

    class Meta:
        db_table = 'concursos'
        
class Inscripcion(models.Model):
    idInscripcion = models.AutoField(primary_key=True)
    idConcurso = models.ForeignKey(Concurso, db_column='idconcurso')
    idOferta = models.ForeignKey(Oferta, db_column='idoferta')
    fecha = models.DateField(db_column='fechainscripcion')
    estado = models.ForeignKey(Catalogo, db_column="estado")

    class Meta:
        db_table = 'inscripcion'


class MilestoneConcurso(models.Model):
    idMilestone = models.AutoField(primary_key=True)
    idConcurso = models.ForeignKey(Concurso, db_column='idConcurso')
    fecha_entrega = models.DateField()
    requerimiento = models.CharField(max_length=300)
    peso = models.PositiveIntegerField()
    estado = models.ForeignKey(Catalogo, db_column="estado")

    class Meta:
        db_table = 'milestoneConcurso'


class MilestoneEntregable(models.Model):
    idMilestoneEntregable = models.AutoField(primary_key=True)
    idMilestoneConcurso = models.ForeignKey(MilestoneConcurso, db_column='idmilestoneConcurso')
    idInscripcion = models.ForeignKey(Inscripcion, db_column='idinscripcion')
    fecha_entrega = models.DateField()
    estado = models.ForeignKey(Catalogo, db_column="estado")

    class Meta:
        db_table = 'milestoneentregable'


class Jurado(models.Model):
    idJurado = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(User, db_column='idusuario')
    idConcurso = models.ForeignKey(Concurso, db_column='idConcurso')

    class Meta:
        db_table = 'jurado'


class Calificacion(models.Model):
    idCalificacion = models.AutoField(primary_key=True)
    idJurado = models.ForeignKey(Jurado, db_column='idjurado')
    idMilestoneEntregable = models.ForeignKey(MilestoneEntregable, db_column='idmilestoneEntregable')
    calificacion = models.PositiveIntegerField()
    comentario = models.CharField(max_length=150)


    class Meta:
        db_table = 'calificacion'

