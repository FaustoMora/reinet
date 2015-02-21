from django.db import models

# Create your models here.


class Incubacion(models.Model):
    id = models.AutoField(db_column="idIncubacion",primary_key=True)
    fechaInicio = models.DateField(null=False,auto_now=True,db_column="fechaInicioIncubacion")
    nombre = models.CharField(null=False,max_length=50,db_column="nombreIncubacion")
    alias = models.CharField(null=False,max_length=50,db_column="aliasIncubacion")
    descripcion = models.CharField(null=False,max_length=10L,db_column="descripcionIncubacion")
    condiciones = models.CharField(null=False,max_length=30L,db_column="condicionesIncubacion")
    perfilOfertas = models.CharField(null=False,max_length=30L,db_column="aliasIncubacion")
    tipoOfertas = models.CharField(null=False,max_length=50,db_column="tipoOfertasIncubacion")
    alcance = models.CharField(null=False,max_length=50,db_column="alcanceIncubacion")
    condicionesAdicionales = models.CharField(null=False,max_length=30L,db_column="alcanceIncubacion")
    estado = models.CharField(null=False,max_length=50,db_column="estadoIncubacion")
    razonEstado = models.CharField(null=False,max_length=50,db_column="razonEstadoIncubacion")

    class Meta:
        db_table="Incubacion"

class IncubacionConsultor(models.Model):
    id = models.AutoField(db_column="idIncubacion_Consultor",primary_key=True)
    incubacion = models.ForeignKey(Incubacion,null=True,db_column="incubacion_idIncubacion")

    class Meta:
        db_table="Incubacion_Consultor"

