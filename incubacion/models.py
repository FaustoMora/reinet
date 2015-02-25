from django.db import models
from usuarios.models import Institucion, Persona
from app.models import Catalogo
from ofertaDemanda.models import Oferta


# Create your models here.
class Consultor(models.Model):
    id = models.AutoField(db_column="idConsultor", primary_key=True, null=False)
    usuario = models.ForeignKey(Persona, db_column="usuario_idUsuario", null=False)
    tipo = models.ForeignKey(Catalogo, db_column="tipoConsultor", null=False)

    class Meta:
        db_table = "Consultor"


class Incubacion(models.Model):
    id = models.AutoField(db_column="idIncubacion", primary_key=True, null=False)
    fechaInicio = models.DateField(null=False, auto_now=True, db_column="fechaInicioIncubacion")
    nombre = models.CharField(null=False, max_length=50, db_column="nombreIncubacion")
    alias = models.CharField(null=False, max_length=50, db_column="aliasIncubacion")
    descripcion = models.CharField(null=False, max_length=10L, db_column="descripcionIncubacion")
    condiciones = models.CharField(null=False, max_length=30L, db_column="condicionesIncubacion")
    perfilOfertas = models.CharField(null=False, max_length=30L, db_column="perfilOfertas")
    tipoOfertas = models.ManyToManyField(Catalogo, through="TiposOfertasIncubacion", related_name="tipoOfertas")
    alcance = models.ForeignKey(Catalogo, null=False, db_column="alcanceIncubacion", related_name="alcance")
    condicionesAdicionales = models.CharField(null=False, max_length=30L, db_column="condicionesAdicionales")
    estado = models.ForeignKey(Catalogo, db_column="estadoIncubacion", related_name="estado")
    razonEstado = models.CharField(null=False, max_length=50, db_column="razonEstadoIncubacion")
    fechaCambioEstado = models.DateField(null=True, db_column="fechaCambioEstado")
    autor = models.ForeignKey(Institucion, null=False, db_column="institucionAutor", related_name="autor")
    invitaciones_consultores = models.ManyToManyField(Persona, through="InvitacionConsultor", related_name="invitaciones_consultores")
    consultores = models.ManyToManyField(Consultor, through="IncubacionConsultor")
    imagen = models.ImageField(upload_to='incubacion_media',db_column="imagenIncubacion",null=True)

    class Meta:
        db_table = "Incubacion"

    def countIncubadas(self):
        list = self.incubadas.all()
        return len(list)

class IncubacionConsultor(models.Model):
    id = models.AutoField(db_column="idIncubacion_Consultor", primary_key=True, null=False)
    incubacion = models.ForeignKey(Incubacion, null=False, db_column="incubacion_idIncubacion")
    consultor = models.ForeignKey(Consultor, null=False, db_column="consultor_idConsultor")

    class Meta:
        db_table = "Incubacion_Consultor"


class InvitacionConsultor(models.Model):
    id = models.AutoField(db_column="idInvitacionConsultor", primary_key=True, null=False)
    incubacion = models.ForeignKey(Incubacion, null=False, db_column="incubacion_idIncubacion")
    invitado = models.ForeignKey(Persona, null=False, db_column="persona_idPersona")
    estado = models.ForeignKey(Catalogo, null=False, db_column="estadoInvitacionIncubacion")

    class Meta:
        db_table = "InvitacionConsultor"


class Milestone(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idMilestone")
    fechaCumplimiento = models.DateField(null=False, db_column="fechaVencimiento")
    requerimientosActuales = models.CharField(max_length=10L, db_column="requerimientosActuales")
    total = models.DecimalField(max_digits=1, decimal_places=1, db_column="calificacionTotalMilestone")

    class Meta:
        db_table = "MilestoneIncubacion"


class Incubada(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idIncubada")
    incubacion = models.ForeignKey(Incubacion, null=False, db_column="incubacion_id_incubacion",related_name="incubadas")
    oferta = models.ForeignKey(Oferta, null=False, db_column="oferta_idOferta")
    consultores = models.ManyToManyField(Consultor, through="ConsultorIncubada")
    milestones = models.ManyToManyField(Milestone, through="IncubadaMilestone")

    class Meta:
        db_table = "Incubada"


class ConsultorIncubada(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idConsultorIncubada")
    consultor = models.ForeignKey(Consultor, null=False, db_column="usuario_idUsuario")
    incubada = models.ForeignKey(Incubada, null=False, db_column="incubada_idIncubada")

    class Meta:
        db_table = "ConsultorIncubada"


class IncubadaMilestone(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idIncubada_Milestone")
    incubada = models.ForeignKey(Incubada, null=False, db_column="incubada_idIncubada")
    milestone = models.ForeignKey(Milestone, null=False, db_column="milestone_idMIlestone")

    class Meta:
        db_table = "Incubada_Milestone"


class CamposAdicionalesMilestone(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idCamposAdicionalesMilestone")
    milestone = models.ForeignKey(Milestone, null=False, db_column="Milestone_idMilestone")
    descripcion = models.CharField(null=False, max_length=300, db_column="descripcionCamposAdicionalesMilestone")
    """importancia = models.ForeignKey(Catalogo, null=False, db_column="importanciaCamposAdicionales")"""

    class Meta:
        db_table = "CamposAdicionalesMilestone"


class Retroalimentacion(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="idRetroalimentacion")
    consultor = models.ForeignKey(Consultor, null=False, db_column="Consultor_idConsultor")
    milestone = models.ForeignKey(Milestone, null=True, db_column="Milestone_idMilestone")
    incubada = models.ForeignKey(Incubada, null=True, db_column="Incubada_idIncubada")
    mensaje = models.CharField(max_length=30L, null=False, db_column="mensajeRetroalimentacion")
    calificacionMilestone = models.IntegerField(null=True, db_column="calificacionMilestone")

    class Meta:
        db_table = "Retroalimentacion"


class ConvocatoriaIncubacion(models.Model):
    id = models.AutoField(primary_key=True, null=False, db_column="ConvocatoriaIncubacion")
    incubacion = models.ForeignKey(Incubacion, null=False, db_column="incubacion_idIncubacion")
    fechaInicio = models.DateField(null=False, db_column="fechaInicioConvocatoria")
    fechaFin = models.DateField(null=False, db_column="fechaFinConvocatoria")

    class Meta:
        db_table = "ConvocatoriaIncubacion"


class ConvocatoriaIncubacionOfertas(models.Model):
    id = models.AutoField(null=False, primary_key=True, db_column="idConvocatoriaIncubacion_Oferta")
    convocatoria = models.ForeignKey(ConvocatoriaIncubacion, null=False, db_column="ConvocatoriaIncubacion_idConvocatoriaIncubacion", related_name="convocatoria")
    oferta = models.ForeignKey(Oferta, null=False, db_column="oferta_idOferta")
    estado = models.ForeignKey(Catalogo, null=False, db_column="estadoSolicitud", related_name="estado_solicitud")

    class Meta:
        db_table = "ConvocatoriaIncubacion_Oferta"


class TiposOfertasIncubacion(models.Model):
    id = models.AutoField(null=False, primary_key=True, db_column="idTipoOfertas_Incubacion")
    incubacion = models.ForeignKey(Incubacion, null=False, db_column="incubacion_idIncubacion")
    tipo = models.ForeignKey(Catalogo, null=False, db_column="catalogo_idCatalogo")

    class Meta:
        db_table = "TipoOfertas_Incubacion"
