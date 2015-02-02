# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80L, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50L)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100L)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128L)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=30L, unique=True)
    first_name = models.CharField(max_length=30L)
    last_name = models.CharField(max_length=30L)
    email = models.CharField(max_length=75L)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Catalogo(models.Model):
    idcatalogo = models.BigIntegerField(primary_key=True)
    codigo = models.CharField(max_length=10L, blank=True)
    descripcion = models.CharField(max_length=100L, blank=True)
    idcatalogopadre = models.ForeignKey('self', null=True, db_column='idcatalogopadre', blank=True)
    class Meta:
        db_table = 'catalogo'

class Comentario(models.Model):
    idcomentario = models.BigIntegerField(unique=True)
    idusuario = models.ForeignKey('AuthUser', db_column='id')
    comentario = models.CharField(max_length=500L)
    calificacion = models.IntegerField(null=True, blank=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    class Meta:
        db_table = 'comentario'

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

class Detalleincubacion(models.Model):
    iddetalleincubacion = models.BigIntegerField(unique=True, db_column='idDetalleIncubacion') # Field name made lowercase.
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    fecha_inicio = models.DateField()
    condiciones = models.CharField(max_length=300L)
    perfil_oferta = models.IntegerField()
    tipo_oferta = models.IntegerField()
    class Meta:
        db_table = 'detalleincubacion'

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

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100L)
    app_label = models.CharField(max_length=100L)
    model = models.CharField(max_length=100L)
    class Meta:
        db_table = 'django_content_type'

class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)
    app = models.CharField(max_length=255L)
    name = models.CharField(max_length=255L)
    applied = models.DateTimeField()
    class Meta:
        db_table = 'django_migrations'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40L, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100L)
    name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'django_site'

class Equipo(models.Model):
    idequipo = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    idusuario = models.ForeignKey('AuthUser', db_column='id')
    rol = models.CharField(max_length=100L)
    class Meta:
        db_table = 'equipo'

class Imagen(models.Model):
    idimagen = models.BigIntegerField(primary_key=True)
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    enlace_imagen = models.CharField(max_length=100L)
    class Meta:
        db_table = 'imagen'

class Institucion(models.Model):
    idinstitucion = models.BigIntegerField(primary_key=True)
    nombre_corto = models.CharField(max_length=20L)
    descripcion = models.CharField(max_length=900L)
    mision = models.CharField(max_length=900L)
    sitio_web = models.CharField(max_length=200L)
    persona_que_registra = models.CharField(max_length=200L)
    idadministrador = models.BigIntegerField(db_column='idAdministrador') # Field name made lowercase.
    email = models.CharField(max_length=50L)
    telefono = models.CharField(max_length=15L)
    recursos = models.CharField(max_length=100L)
    idusuario = models.ForeignKey('AuthUser', db_column='id')
    class Meta:
        db_table = 'institucion'

class InstitucionPersona(models.Model):
    idpersona = models.ForeignKey('Persona', db_column='idpersona')
    idinstitucion = models.ForeignKey(Institucion, db_column='idinstitucion')
    class Meta:
        db_table = 'institucion_persona'

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

class Persona(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='persona')
    idpersona = models.BigIntegerField(primary_key=True)
    identificacion = models.CharField(max_length=20L)
    cargo = models.CharField(max_length=50L)
    actividad = models.CharField(max_length=150L)
    fecha_nacimiento = models.DateField()
    areas_interes = models.CharField(max_length=50L)
    #idusuario = models.ForeignKey(AuthUser, db_column='id')
    class Meta:
        db_table = 'persona'

class Politicaprivacidad(models.Model):
    idusuario = models.ForeignKey('AuthUser', db_column='id')
    idpublicacion = models.ForeignKey('Publicacion', db_column='idpublicacion')
    tipo_alcance = models.CharField(max_length=50L)
    class Meta:
        db_table = 'politicaprivacidad'

class Publicacion(models.Model):
    idpublicacion = models.BigIntegerField(unique=True)
    idusuario = models.ForeignKey('AuthUser', db_column='id')
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

