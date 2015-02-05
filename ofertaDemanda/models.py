from django.db import models
"""
# Create your models here. OFERTA DEMANDA
class Detalledemanda(models.Model):
    iddetalledemanda = models.BigIntegerField(unique=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion', related_name='detalle_publicacion')
    palabras_claves = models.CharField(max_length=100L, db_column='palabras_Claves') # Field name made lowercase.
    tiempo_inicio_disponible = models.DateField(db_column='tiempo_Inicio_Disponible') # Field name made lowercase.
    tiempo_fin_disponible = models.DateField(db_column='tiempo_Fin_Disponible') # Field name made lowercase.
    lugar_aplicacion = models.CharField(max_length=200L, db_column='lugar_Aplicacion') # Field name made lowercase.
    perfil_beneficiario = models.CharField(max_length=500L, db_column='perfil_Beneficiario') # Field name made lowercase.
    perfil_cliente = models.CharField(max_length=500L, db_column='perfil_Cliente') # Field name made lowercase.
    soluciones_alternativas = models.CharField(max_length=500L, db_column='soluciones_Alternativas') # Field name made lowercase.
    importancia_solucion = models.CharField(max_length=500L, db_column='importancia_Solucion') # Field name made lowercase.
    class Meta:
        db_table = 'detalledemanda'


class Detalleoferta(models.Model):
    iddetalleoferta = models.BigIntegerField(unique=True)
    idpublicacion = models.ForeignKey('Publicacion', null=True, db_column='idpublicacion', blank=True)
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
        db_table = 'detalleoferta'



class Diagramacanvas(models.Model):
    iddiagramacanvas = models.BigIntegerField(primary_key=True, db_column='idDiagramaCanvas') # Field name made lowercase.
    iddetalleoferta = models.ForeignKey(Detalleoferta, db_column='iddetalleoferta')
    asociacionesclave = models.CharField(max_length=150L, db_column='asociacionesClave') # Field name made lowercase.
    actividadesclave = models.CharField(max_length=150L, db_column='actividadesClave') # Field name made lowercase.
    recursosclave = models.CharField(max_length=150L, db_column='recursosClave') # Field name made lowercase.
    propuestavalor = models.CharField(max_length=150L, db_column='propuestaValor') # Field name made lowercase.
    relacionclientes = models.CharField(max_length=150L, db_column='relacionClientes') # Field name made lowercase.
    segmentomercado = models.CharField(max_length=150L, db_column='segmentoMercado') # Field name made lowercase.
    estructuracostos = models.CharField(max_length=150L, db_column='estructuraCostos') # Field name made lowercase.
    fuenteingresos = models.CharField(max_length=150L, db_column='fuenteIngresos') # Field name made lowercase.
    class Meta:
        db_table = 'diagramacanvas'

class Diagramaporter(models.Model):
    iddiagramaporter = models.BigIntegerField(primary_key=True, db_column='iddiagramaPorter') # Field name made lowercase.
    iddetalleoferta = models.ForeignKey(Detalleoferta, db_column='iddetalleoferta')
    rivalidadcompetidores = models.CharField(max_length=200L, db_column='rivalidadCompetidores') # Field name made lowercase.
    competidorespotenciales = models.CharField(max_length=200L, db_column='competidoresPotenciales') # Field name made lowercase.
    proveedores = models.CharField(max_length=200L)
    sustitutos = models.CharField(max_length=200L)
    consumidores = models.CharField(max_length=200L)
    class Meta:
        db_table = 'diagramaporter'

"""