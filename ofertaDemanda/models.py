from django.db import models
from app.models import *
from usuarios.models import *
# Create your models here. OFERTA DEMANDA

class Demanda(models.Model):    
    idDemanda = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(User, db_column='idusuario')
    nombre = models.CharField(max_length=150L,blank=False)
    descripcion = models.CharField(max_length=500L,blank=False)
    dominio = models.IntegerField(blank=False)
    subdominio = models.IntegerField(blank=False)
    palabras_claves = models.CharField(max_length=100L, db_column='palabras_Claves') # Field name made lowercase.
    tiempo_inicio_disponible = models.DateField(db_column='tiempo_Inicio_Disponible') # Field name made lowercase.
    tiempo_fin_disponible = models.DateField(db_column='tiempo_Fin_Disponible') # Field name made lowercase.
    lugar_aplicacion = models.CharField(max_length=200L, db_column='lugar_Aplicacion') # Field name made lowercase.
    perfil_beneficiario = models.CharField(max_length=500L, db_column='perfil_Beneficiario') # Field name made lowercase.
    perfil_cliente = models.CharField(max_length=500L, db_column='perfil_Cliente') # Field name made lowercase.
    soluciones_alternativas = models.CharField(max_length=500L, db_column='soluciones_Alternativas') # Field name made lowercase.
    importancia_solucion = models.CharField(max_length=500L, db_column='importancia_Solucion') # Field name made lowercase.
    class Meta:
        db_table = 'demanda'

class ComentarioDemanda(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    idDemanda = models.ForeignKey(Demanda, db_column='idDemanda')
    idusuario = models.ForeignKey(Persona, db_column='idpersona')
    comentario = models.CharField(max_length=500L)
    calificacion = models.IntegerField()    
    class Meta:
        db_table = 'comentarioDemanda'

class ImagenDemanda(models.Model):
    idimagen = models.AutoField(primary_key=True)
    idDemanda = models.ForeignKey(Demanda, db_column='idDemanda')
    enlace_imagen = models.CharField(max_length=100L)
    class Meta:
        db_table = 'imagenDemanda'

class Oferta(models.Model):
    idOferta = models.AutoField(primary_key=True)
    idusuario = models.ForeignKey(User, db_column='idusuario')
    estadoOferta= models.IntegerField()
    calificacionGeneral = models.IntegerField(null=True)
    ofertaPublicada = models.BooleanField()
    nombre = models.CharField(max_length=150L,blank=False)
    descripcion = models.CharField(max_length=500L,blank=False)
    dominio = models.IntegerField(blank=False)
    subdominio = models.IntegerField()
    palabras_claves = models.CharField(max_length=100L, db_column='palabras_Claves') # Field name made lowercase.
    tiempo_inicio_disponible = models.DateField(db_column='tiempo_Inicio_Disponible') # Field name made lowercase.
    tiempo_fin_disponible = models.DateField(db_column='tiempo_Fin_Disponible') # Field name made lowercase.
    lugar_aplicacion = models.CharField(max_length=200L, db_column='lugar_Aplicacion') # Field name made lowercase.
    perfil_beneficiario = models.CharField(max_length=500L, db_column='perfil_Beneficiario') # Field name made lowercase.
    perfil_cliente = models.CharField(max_length=500L, db_column='perfil_Cliente') # Field name made lowercase.
    soluciones_alternativas = models.CharField(max_length=500L, db_column='soluciones_Alternativas', blank=True) # Field name made lowercase.
    propuesta_valor = models.CharField(max_length=300L, db_column='propuesta_Valor', blank=True) # Field name made lowercase.
    cuadro_competidores = models.CharField(max_length=100L, db_column='cuadro_Competidores', blank=True) # Field name made lowercase.
    cuadro_tendencias_relevantes = models.CharField(max_length=100L, db_column='cuadro_Tendencias_Relevantes', blank=True) # Field name made lowercase.
    estado_propiedad_intelectual = models.CharField(max_length=500L, db_column='estado_Propiedad_Intelectual', blank=True) # Field name made lowercase.
    evidencia_traccion = models.CharField(max_length=500L, db_column='evidencia_Traccion', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'oferta'


class Diagramacanvas(models.Model):
    iddiagramacanvas = models.AutoField(primary_key=True) # Field name made lowercase.
    idOferta = models.ForeignKey(Oferta, db_column='idOferta')
    asociacionesclave = models.CharField(max_length=150L, db_column='asociacionesClave',null=True) # Field name made lowercase.
    actividadesclave = models.CharField(max_length=150L, db_column='actividadesClave',null=True) # Field name made lowercase.
    recursosclave = models.CharField(max_length=150L, db_column='recursosClave',null=True) # Field name made lowercase.
    propuestavalor = models.CharField(max_length=150L, db_column='propuestaValor',null=True) # Field name made lowercase.
    relacionclientes = models.CharField(max_length=150L, db_column='relacionClientes',null=True) # Field name made lowercase.
    segmentomercado = models.CharField(max_length=150L, db_column='segmentoMercado',null=True) # Field name made lowercase.
    estructuracostos = models.CharField(max_length=150L, db_column='estructuraCostos',null=True) # Field name made lowercase.
    fuenteingresos = models.CharField(max_length=150L, db_column='fuenteIngresos',null=True) # Field name made lowercase.
    class Meta:
        db_table = 'diagramacanvas'

class Diagramaporter(models.Model):
    iddiagramaporter = models.AutoField(primary_key=True, db_column='iddiagramaPorter') # Field name made lowercase.
    idOferta = models.ForeignKey(Oferta, db_column='idOferta')
    rivalidadcompetidores = models.CharField(max_length=200L, db_column='rivalidadCompetidores',null=True) # Field name made lowercase.
    competidorespotenciales = models.CharField(max_length=200L, db_column='competidoresPotenciales',null=True) # Field name made lowercase.
    proveedores = models.CharField(max_length=200L,null=True)
    sustitutos = models.CharField(max_length=200L,null=True)
    consumidores = models.CharField(max_length=200L,null=True)
    class Meta:
        db_table = 'diagramaporter'

class Equipo(models.Model):
    idequipo = models.AutoField(primary_key=True)
    idofertaEquipo = models.ForeignKey(Oferta, db_column='idOferta')
    idusuario = models.ForeignKey(Persona, db_column='idpersona')
    rol = models.CharField(max_length=100L)
    estado=models.IntegerField()
    class Meta:
        db_table = 'equipo'

class SolicitudEquipo(models.Model):
    idSolicitudEquipo = models.AutoField(primary_key=True)
    idEquipoSolicitud = models.ForeignKey(Equipo, db_column='idequipo')
    idusuario = models.ForeignKey(Persona, db_column='idpersona')
    pendienteRevision = models.BooleanField()
    aprobada=models.BooleanField()  
    class Meta:
        db_table = 'solicitudEquipo'

class ImagenOferta(models.Model):
    idimagen = models.AutoField(primary_key=True)
    idOferta = models.ForeignKey(Oferta, db_column='idOferta')
    enlace_imagen = models.CharField(max_length=100L)
    class Meta:
        db_table = 'imagenOferta'

class ComentarioOferta(models.Model):
    idcomentario = models.AutoField(primary_key=True)
    idOferta = models.ForeignKey(Oferta, db_column='idOferta')
    idusuario = models.ForeignKey(Persona, db_column='idpersona')
    comentario = models.CharField(max_length=500L)
    calificacion = models.IntegerField()
    pendienteRevision = models.BooleanField()
    aprobado=models.BooleanField()  
    class Meta:
        db_table = 'comentarioOferta'

#null=True, blank=True