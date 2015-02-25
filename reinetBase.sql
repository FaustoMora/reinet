-- MySQL dump 10.13  Distrib 5.6.19, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: redinnovacion
-- ------------------------------------------------------
-- Server version	5.6.19-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `CamposAdicionalesMilestone`
--

DROP TABLE IF EXISTS `CamposAdicionalesMilestone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CamposAdicionalesMilestone` (
  `idCamposAdicionalesMilestone` int(11) NOT NULL AUTO_INCREMENT,
  `Milestone_idMilestone` int(11) NOT NULL,
  `descripcionCamposAdicionalesMilestone` varchar(300) NOT NULL,
  PRIMARY KEY (`idCamposAdicionalesMilestone`),
  KEY `CamposAdicionalesMilestone_97058a4c` (`Milestone_idMilestone`),
  CONSTRAINT `Milestone_idMilestone_refs_idMilestone_e91ee2d3` FOREIGN KEY (`Milestone_idMilestone`) REFERENCES `MilestoneIncubacion` (`idMilestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CamposAdicionalesMilestone`
--

LOCK TABLES `CamposAdicionalesMilestone` WRITE;
/*!40000 ALTER TABLE `CamposAdicionalesMilestone` DISABLE KEYS */;
/*!40000 ALTER TABLE `CamposAdicionalesMilestone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Catalogo`
--

DROP TABLE IF EXISTS `Catalogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Catalogo` (
  `idCatalogo` int(11) NOT NULL AUTO_INCREMENT,
  `codigoCatalogo` varchar(30) NOT NULL,
  `descripcionCatalogo` varchar(100) NOT NULL,
  `idcatalogopadre` int(11) DEFAULT NULL,
  PRIMARY KEY (`idCatalogo`),
  KEY `Catalogo_b475db24` (`idcatalogopadre`),
  CONSTRAINT `idcatalogopadre_refs_idCatalogo_6df36458` FOREIGN KEY (`idcatalogopadre`) REFERENCES `Catalogo` (`idCatalogo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Catalogo`
--

LOCK TABLES `Catalogo` WRITE;
/*!40000 ALTER TABLE `Catalogo` DISABLE KEYS */;
/*!40000 ALTER TABLE `Catalogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Consultor`
--

DROP TABLE IF EXISTS `Consultor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Consultor` (
  `idConsultor` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_idUsuario` int(11) NOT NULL,
  `tipoConsultor` int(11) NOT NULL,
  PRIMARY KEY (`idConsultor`),
  KEY `Consultor_c69e2c81` (`usuario_idUsuario`),
  KEY `Consultor_acf1eac4` (`tipoConsultor`),
  CONSTRAINT `usuario_idUsuario_refs_idpersona_49caa6a6` FOREIGN KEY (`usuario_idUsuario`) REFERENCES `persona` (`idpersona`),
  CONSTRAINT `tipoConsultor_refs_idCatalogo_3e4f50f0` FOREIGN KEY (`tipoConsultor`) REFERENCES `Catalogo` (`idCatalogo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Consultor`
--

LOCK TABLES `Consultor` WRITE;
/*!40000 ALTER TABLE `Consultor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Consultor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ConsultorIncubada`
--

DROP TABLE IF EXISTS `ConsultorIncubada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ConsultorIncubada` (
  `idConsultorIncubada` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_idUsuario` int(11) NOT NULL,
  `incubada_idIncubada` int(11) NOT NULL,
  PRIMARY KEY (`idConsultorIncubada`),
  KEY `ConsultorIncubada_eb9ec788` (`usuario_idUsuario`),
  KEY `ConsultorIncubada_72aa7ede` (`incubada_idIncubada`),
  CONSTRAINT `usuario_idUsuario_refs_idConsultor_444f88b3` FOREIGN KEY (`usuario_idUsuario`) REFERENCES `Consultor` (`idConsultor`),
  CONSTRAINT `incubada_idIncubada_refs_idIncubada_6ce38ec9` FOREIGN KEY (`incubada_idIncubada`) REFERENCES `Incubada` (`idIncubada`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ConsultorIncubada`
--

LOCK TABLES `ConsultorIncubada` WRITE;
/*!40000 ALTER TABLE `ConsultorIncubada` DISABLE KEYS */;
/*!40000 ALTER TABLE `ConsultorIncubada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ConvocatoriaIncubacion`
--

DROP TABLE IF EXISTS `ConvocatoriaIncubacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ConvocatoriaIncubacion` (
  `ConvocatoriaIncubacion` int(11) NOT NULL AUTO_INCREMENT,
  `incubacion_idIncubacion` int(11) NOT NULL,
  `fechaInicioConvocatoria` date NOT NULL,
  `fechaFinConvocatoria` date NOT NULL,
  PRIMARY KEY (`ConvocatoriaIncubacion`),
  KEY `ConvocatoriaIncubacion_82d85dc2` (`incubacion_idIncubacion`),
  CONSTRAINT `incubacion_idIncubacion_refs_idIncubacion_4592bfc6` FOREIGN KEY (`incubacion_idIncubacion`) REFERENCES `Incubacion` (`idIncubacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ConvocatoriaIncubacion`
--

LOCK TABLES `ConvocatoriaIncubacion` WRITE;
/*!40000 ALTER TABLE `ConvocatoriaIncubacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `ConvocatoriaIncubacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ConvocatoriaIncubacion_Oferta`
--

DROP TABLE IF EXISTS `ConvocatoriaIncubacion_Oferta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ConvocatoriaIncubacion_Oferta` (
  `idConvocatoriaIncubacion_Oferta` int(11) NOT NULL AUTO_INCREMENT,
  `ConvocatoriaIncubacion_idConvocatoriaIncubacion` int(11) NOT NULL,
  `oferta_idOferta` int(11) NOT NULL,
  `estadoSolicitud` int(11) NOT NULL,
  PRIMARY KEY (`idConvocatoriaIncubacion_Oferta`),
  KEY `ConvocatoriaIncubacion_Oferta_51d63455` (`ConvocatoriaIncubacion_idConvocatoriaIncubacion`),
  KEY `ConvocatoriaIncubacion_Oferta_72d14715` (`oferta_idOferta`),
  KEY `ConvocatoriaIncubacion_Oferta_eeec61f0` (`estadoSolicitud`),
  CONSTRAINT `oferta_idOferta_refs_idOferta_b3a9daf8` FOREIGN KEY (`oferta_idOferta`) REFERENCES `oferta` (`idOferta`),
  CONSTRAINT `ConvocatoriaIncubacion_idConvocatoriaIncubacion_refs_Convoca9db6` FOREIGN KEY (`ConvocatoriaIncubacion_idConvocatoriaIncubacion`) REFERENCES `ConvocatoriaIncubacion` (`ConvocatoriaIncubacion`),
  CONSTRAINT `estadoSolicitud_refs_idCatalogo_e028b9d2` FOREIGN KEY (`estadoSolicitud`) REFERENCES `Catalogo` (`idCatalogo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ConvocatoriaIncubacion_Oferta`
--

LOCK TABLES `ConvocatoriaIncubacion_Oferta` WRITE;
/*!40000 ALTER TABLE `ConvocatoriaIncubacion_Oferta` DISABLE KEYS */;
/*!40000 ALTER TABLE `ConvocatoriaIncubacion_Oferta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incubacion`
--

DROP TABLE IF EXISTS `Incubacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incubacion` (
  `idIncubacion` int(11) NOT NULL AUTO_INCREMENT,
  `fechaInicioIncubacion` date NOT NULL,
  `nombreIncubacion` varchar(50) NOT NULL,
  `aliasIncubacion` varchar(50) NOT NULL,
  `descripcionIncubacion` varchar(10) NOT NULL,
  `condicionesIncubacion` varchar(30) NOT NULL,
  `perfilOfertas` varchar(30) NOT NULL,
  `alcanceIncubacion` int(11) NOT NULL,
  `condicionesAdicionales` varchar(30) NOT NULL,
  `estadoIncubacion` int(11) NOT NULL,
  `razonEstadoIncubacion` varchar(50) NOT NULL,
  `fechaCambioEstado` date DEFAULT NULL,
  `institucionAutor` int(11) NOT NULL,
  PRIMARY KEY (`idIncubacion`),
  KEY `Incubacion_834df3a0` (`alcanceIncubacion`),
  KEY `Incubacion_eeec61f0` (`estadoIncubacion`),
  KEY `Incubacion_40e8bcf3` (`institucionAutor`),
  CONSTRAINT `institucionAutor_refs_idinstitucion_1a145b18` FOREIGN KEY (`institucionAutor`) REFERENCES `institucion` (`idinstitucion`),
  CONSTRAINT `alcanceIncubacion_refs_idCatalogo_40889d21` FOREIGN KEY (`alcanceIncubacion`) REFERENCES `Catalogo` (`idCatalogo`),
  CONSTRAINT `estadoIncubacion_refs_idCatalogo_40889d21` FOREIGN KEY (`estadoIncubacion`) REFERENCES `Catalogo` (`idCatalogo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incubacion`
--

LOCK TABLES `Incubacion` WRITE;
/*!40000 ALTER TABLE `Incubacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Incubacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incubacion_Consultor`
--

DROP TABLE IF EXISTS `Incubacion_Consultor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incubacion_Consultor` (
  `idIncubacion_Consultor` int(11) NOT NULL AUTO_INCREMENT,
  `incubacion_idIncubacion` int(11) NOT NULL,
  `consultor_idConsultor` int(11) NOT NULL,
  PRIMARY KEY (`idIncubacion_Consultor`),
  KEY `Incubacion_Consultor_82d85dc2` (`incubacion_idIncubacion`),
  KEY `Incubacion_Consultor_eb9ec788` (`consultor_idConsultor`),
  CONSTRAINT `consultor_idConsultor_refs_idConsultor_7bd3d391` FOREIGN KEY (`consultor_idConsultor`) REFERENCES `Consultor` (`idConsultor`),
  CONSTRAINT `incubacion_idIncubacion_refs_idIncubacion_270b816a` FOREIGN KEY (`incubacion_idIncubacion`) REFERENCES `Incubacion` (`idIncubacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incubacion_Consultor`
--

LOCK TABLES `Incubacion_Consultor` WRITE;
/*!40000 ALTER TABLE `Incubacion_Consultor` DISABLE KEYS */;
/*!40000 ALTER TABLE `Incubacion_Consultor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incubada`
--

DROP TABLE IF EXISTS `Incubada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incubada` (
  `idIncubada` int(11) NOT NULL AUTO_INCREMENT,
  `incubacion_id_incubacion` int(11) NOT NULL,
  `oferta_idOferta` int(11) NOT NULL,
  PRIMARY KEY (`idIncubada`),
  KEY `Incubada_82d85dc2` (`incubacion_id_incubacion`),
  KEY `Incubada_72d14715` (`oferta_idOferta`),
  CONSTRAINT `oferta_idOferta_refs_idOferta_b4573e87` FOREIGN KEY (`oferta_idOferta`) REFERENCES `oferta` (`idOferta`),
  CONSTRAINT `incubacion_id_incubacion_refs_idIncubacion_68929ef6` FOREIGN KEY (`incubacion_id_incubacion`) REFERENCES `Incubacion` (`idIncubacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incubada`
--

LOCK TABLES `Incubada` WRITE;
/*!40000 ALTER TABLE `Incubada` DISABLE KEYS */;
/*!40000 ALTER TABLE `Incubada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Incubada_Milestone`
--

DROP TABLE IF EXISTS `Incubada_Milestone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Incubada_Milestone` (
  `idIncubada_Milestone` int(11) NOT NULL AUTO_INCREMENT,
  `incubada_idIncubada` int(11) NOT NULL,
  `milestone_idMIlestone` int(11) NOT NULL,
  PRIMARY KEY (`idIncubada_Milestone`),
  KEY `Incubada_Milestone_72aa7ede` (`incubada_idIncubada`),
  KEY `Incubada_Milestone_97058a4c` (`milestone_idMIlestone`),
  CONSTRAINT `incubada_idIncubada_refs_idIncubada_f7546baa` FOREIGN KEY (`incubada_idIncubada`) REFERENCES `Incubada` (`idIncubada`),
  CONSTRAINT `milestone_idMIlestone_refs_idMilestone_9060a38f` FOREIGN KEY (`milestone_idMIlestone`) REFERENCES `MilestoneIncubacion` (`idMilestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Incubada_Milestone`
--

LOCK TABLES `Incubada_Milestone` WRITE;
/*!40000 ALTER TABLE `Incubada_Milestone` DISABLE KEYS */;
/*!40000 ALTER TABLE `Incubada_Milestone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InvitacionConsultor`
--

DROP TABLE IF EXISTS `InvitacionConsultor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InvitacionConsultor` (
  `idInvitacionConsultor` int(11) NOT NULL AUTO_INCREMENT,
  `incubacion_idIncubacion` int(11) NOT NULL,
  `persona_idPersona` int(11) NOT NULL,
  `estadoInvitacionIncubacion` int(11) NOT NULL,
  PRIMARY KEY (`idInvitacionConsultor`),
  KEY `InvitacionConsultor_82d85dc2` (`incubacion_idIncubacion`),
  KEY `InvitacionConsultor_62b8d49e` (`persona_idPersona`),
  KEY `InvitacionConsultor_eeec61f0` (`estadoInvitacionIncubacion`),
  CONSTRAINT `persona_idPersona_refs_idpersona_3f011ae7` FOREIGN KEY (`persona_idPersona`) REFERENCES `persona` (`idpersona`),
  CONSTRAINT `estadoInvitacionIncubacion_refs_idCatalogo_52dd7513` FOREIGN KEY (`estadoInvitacionIncubacion`) REFERENCES `Catalogo` (`idCatalogo`),
  CONSTRAINT `incubacion_idIncubacion_refs_idIncubacion_cbcce1a2` FOREIGN KEY (`incubacion_idIncubacion`) REFERENCES `Incubacion` (`idIncubacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InvitacionConsultor`
--

LOCK TABLES `InvitacionConsultor` WRITE;
/*!40000 ALTER TABLE `InvitacionConsultor` DISABLE KEYS */;
/*!40000 ALTER TABLE `InvitacionConsultor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `MilestoneIncubacion`
--

DROP TABLE IF EXISTS `MilestoneIncubacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `MilestoneIncubacion` (
  `idMilestone` int(11) NOT NULL AUTO_INCREMENT,
  `fechaVencimiento` date NOT NULL,
  `requerimientosActuales` varchar(10) NOT NULL,
  `calificacionTotalMilestone` decimal(1,1) NOT NULL,
  PRIMARY KEY (`idMilestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `MilestoneIncubacion`
--

LOCK TABLES `MilestoneIncubacion` WRITE;
/*!40000 ALTER TABLE `MilestoneIncubacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `MilestoneIncubacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Retroalimentacion`
--

DROP TABLE IF EXISTS `Retroalimentacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Retroalimentacion` (
  `idRetroalimentacion` int(11) NOT NULL AUTO_INCREMENT,
  `Consultor_idConsultor` int(11) NOT NULL,
  `Milestone_idMilestone` int(11) DEFAULT NULL,
  `Incubada_idIncubada` int(11) DEFAULT NULL,
  `mensajeRetroalimentacion` varchar(30) NOT NULL,
  `calificacionMilestone` int(11) DEFAULT NULL,
  PRIMARY KEY (`idRetroalimentacion`),
  KEY `Retroalimentacion_eb9ec788` (`Consultor_idConsultor`),
  KEY `Retroalimentacion_97058a4c` (`Milestone_idMilestone`),
  KEY `Retroalimentacion_72aa7ede` (`Incubada_idIncubada`),
  CONSTRAINT `Consultor_idConsultor_refs_idConsultor_c7c08bf5` FOREIGN KEY (`Consultor_idConsultor`) REFERENCES `Consultor` (`idConsultor`),
  CONSTRAINT `Incubada_idIncubada_refs_idIncubada_3ce566c3` FOREIGN KEY (`Incubada_idIncubada`) REFERENCES `Incubada` (`idIncubada`),
  CONSTRAINT `Milestone_idMilestone_refs_idMilestone_0fc15c87` FOREIGN KEY (`Milestone_idMilestone`) REFERENCES `MilestoneIncubacion` (`idMilestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Retroalimentacion`
--

LOCK TABLES `Retroalimentacion` WRITE;
/*!40000 ALTER TABLE `Retroalimentacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Retroalimentacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `TipoOfertas_Incubacion`
--

DROP TABLE IF EXISTS `TipoOfertas_Incubacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `TipoOfertas_Incubacion` (
  `idTipoOfertas_Incubacion` int(11) NOT NULL AUTO_INCREMENT,
  `incubacion_idIncubacion` int(11) NOT NULL,
  `catalogo_idCatalogo` int(11) NOT NULL,
  PRIMARY KEY (`idTipoOfertas_Incubacion`),
  KEY `TipoOfertas_Incubacion_82d85dc2` (`incubacion_idIncubacion`),
  KEY `TipoOfertas_Incubacion_acf1eac4` (`catalogo_idCatalogo`),
  CONSTRAINT `incubacion_idIncubacion_refs_idIncubacion_46788758` FOREIGN KEY (`incubacion_idIncubacion`) REFERENCES `Incubacion` (`idIncubacion`),
  CONSTRAINT `catalogo_idCatalogo_refs_idCatalogo_07fa446e` FOREIGN KEY (`catalogo_idCatalogo`) REFERENCES `Catalogo` (`idCatalogo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `TipoOfertas_Incubacion`
--

LOCK TABLES `TipoOfertas_Incubacion` WRITE;
/*!40000 ALTER TABLE `TipoOfertas_Incubacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `TipoOfertas_Incubacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add catalogo',7,'add_catalogo'),(20,'Can change catalogo',7,'change_catalogo'),(21,'Can delete catalogo',7,'delete_catalogo'),(22,'Can add publicacion',8,'add_publicacion'),(23,'Can change publicacion',8,'change_publicacion'),(24,'Can delete publicacion',8,'delete_publicacion'),(25,'Can add concurso',9,'add_concurso'),(26,'Can change concurso',9,'change_concurso'),(27,'Can delete concurso',9,'delete_concurso'),(28,'Can add inscripcion',10,'add_inscripcion'),(29,'Can change inscripcion',10,'change_inscripcion'),(30,'Can delete inscripcion',10,'delete_inscripcion'),(31,'Can add milestone concurso',11,'add_milestoneconcurso'),(32,'Can change milestone concurso',11,'change_milestoneconcurso'),(33,'Can delete milestone concurso',11,'delete_milestoneconcurso'),(34,'Can add milestone entregable',12,'add_milestoneentregable'),(35,'Can change milestone entregable',12,'change_milestoneentregable'),(36,'Can delete milestone entregable',12,'delete_milestoneentregable'),(37,'Can add jurado',13,'add_jurado'),(38,'Can change jurado',13,'change_jurado'),(39,'Can delete jurado',13,'delete_jurado'),(40,'Can add calificacion',14,'add_calificacion'),(41,'Can change calificacion',14,'change_calificacion'),(42,'Can delete calificacion',14,'delete_calificacion'),(43,'Can add institucion',15,'add_institucion'),(44,'Can change institucion',15,'change_institucion'),(45,'Can delete institucion',15,'delete_institucion'),(46,'Can add persona',16,'add_persona'),(47,'Can change persona',16,'change_persona'),(48,'Can delete persona',16,'delete_persona'),(49,'Can add institucion persona',17,'add_institucionpersona'),(50,'Can change institucion persona',17,'change_institucionpersona'),(51,'Can delete institucion persona',17,'delete_institucionpersona'),(52,'Can add mensaje',18,'add_mensaje'),(53,'Can change mensaje',18,'change_mensaje'),(54,'Can delete mensaje',18,'delete_mensaje'),(55,'Can add demanda',19,'add_demanda'),(56,'Can change demanda',19,'change_demanda'),(57,'Can delete demanda',19,'delete_demanda'),(58,'Can add comentario demanda',20,'add_comentariodemanda'),(59,'Can change comentario demanda',20,'change_comentariodemanda'),(60,'Can delete comentario demanda',20,'delete_comentariodemanda'),(61,'Can add imagen demanda',21,'add_imagendemanda'),(62,'Can change imagen demanda',21,'change_imagendemanda'),(63,'Can delete imagen demanda',21,'delete_imagendemanda'),(64,'Can add oferta',22,'add_oferta'),(65,'Can change oferta',22,'change_oferta'),(66,'Can delete oferta',22,'delete_oferta'),(67,'Can add diagramacanvas',23,'add_diagramacanvas'),(68,'Can change diagramacanvas',23,'change_diagramacanvas'),(69,'Can delete diagramacanvas',23,'delete_diagramacanvas'),(70,'Can add diagramaporter',24,'add_diagramaporter'),(71,'Can change diagramaporter',24,'change_diagramaporter'),(72,'Can delete diagramaporter',24,'delete_diagramaporter'),(73,'Can add equipo',25,'add_equipo'),(74,'Can change equipo',25,'change_equipo'),(75,'Can delete equipo',25,'delete_equipo'),(76,'Can add solicitud equipo',26,'add_solicitudequipo'),(77,'Can change solicitud equipo',26,'change_solicitudequipo'),(78,'Can delete solicitud equipo',26,'delete_solicitudequipo'),(79,'Can add imagen oferta',27,'add_imagenoferta'),(80,'Can change imagen oferta',27,'change_imagenoferta'),(81,'Can delete imagen oferta',27,'delete_imagenoferta'),(82,'Can add comentario oferta',28,'add_comentariooferta'),(83,'Can change comentario oferta',28,'change_comentariooferta'),(84,'Can delete comentario oferta',28,'delete_comentariooferta'),(85,'Can add consultor',29,'add_consultor'),(86,'Can change consultor',29,'change_consultor'),(87,'Can delete consultor',29,'delete_consultor'),(88,'Can add incubacion',30,'add_incubacion'),(89,'Can change incubacion',30,'change_incubacion'),(90,'Can delete incubacion',30,'delete_incubacion'),(91,'Can add incubacion consultor',31,'add_incubacionconsultor'),(92,'Can change incubacion consultor',31,'change_incubacionconsultor'),(93,'Can delete incubacion consultor',31,'delete_incubacionconsultor'),(94,'Can add invitacion consultor',32,'add_invitacionconsultor'),(95,'Can change invitacion consultor',32,'change_invitacionconsultor'),(96,'Can delete invitacion consultor',32,'delete_invitacionconsultor'),(97,'Can add milestone',33,'add_milestone'),(98,'Can change milestone',33,'change_milestone'),(99,'Can delete milestone',33,'delete_milestone'),(100,'Can add incubada',34,'add_incubada'),(101,'Can change incubada',34,'change_incubada'),(102,'Can delete incubada',34,'delete_incubada'),(103,'Can add consultor incubada',35,'add_consultorincubada'),(104,'Can change consultor incubada',35,'change_consultorincubada'),(105,'Can delete consultor incubada',35,'delete_consultorincubada'),(106,'Can add incubada milestone',36,'add_incubadamilestone'),(107,'Can change incubada milestone',36,'change_incubadamilestone'),(108,'Can delete incubada milestone',36,'delete_incubadamilestone'),(109,'Can add campos adicionales milestone',37,'add_camposadicionalesmilestone'),(110,'Can change campos adicionales milestone',37,'change_camposadicionalesmilestone'),(111,'Can delete campos adicionales milestone',37,'delete_camposadicionalesmilestone'),(112,'Can add retroalimentacion',38,'add_retroalimentacion'),(113,'Can change retroalimentacion',38,'change_retroalimentacion'),(114,'Can delete retroalimentacion',38,'delete_retroalimentacion'),(115,'Can add convocatoria incubacion',39,'add_convocatoriaincubacion'),(116,'Can change convocatoria incubacion',39,'change_convocatoriaincubacion'),(117,'Can delete convocatoria incubacion',39,'delete_convocatoriaincubacion'),(118,'Can add convocatoria incubacion ofertas',40,'add_convocatoriaincubacionofertas'),(119,'Can change convocatoria incubacion ofertas',40,'change_convocatoriaincubacionofertas'),(120,'Can delete convocatoria incubacion ofertas',40,'delete_convocatoriaincubacionofertas'),(121,'Can add tipos ofertas incubacion',41,'add_tiposofertasincubacion'),(122,'Can change tipos ofertas incubacion',41,'change_tiposofertasincubacion'),(123,'Can delete tipos ofertas incubacion',41,'delete_tiposofertasincubacion');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$8JdjAUPYUYRk$CNUzfqKYkDOE8T1i47abHqjn0nhpoxl53+0C9dhx6Y8=','2015-02-25 17:24:05',0,'adguale','Angel','Guale','xngelguale@yahoo.com',0,1,'2015-02-25 09:44:50'),(2,'pbkdf2_sha256$10000$nvltfY3GxLEW$vc03tZ6n9pNvWnlAJXpenGdDywvhDpFZJvpuaIbuvlY=','2015-02-25 09:55:05',0,'Espol','Espol','','adguale2@espol.edu.ec',0,1,'2015-02-25 09:54:59'),(3,'pbkdf2_sha256$10000$uKXneN8cmwMI$tW4C0BCmT2ngYKslLB66lSr84/RMS4qG0HaewJeyTeg=','2015-02-25 17:15:46',0,'faustomora','fausto','mora','lalalaa@gmail.com',0,1,'2015-02-25 17:15:27'),(4,'pbkdf2_sha256$10000$oKFNFOfBOPY5$epq/evfA/hO73wg4pYj2rwjDX+cIXILkvr0U8P8Svco=','2015-02-25 17:16:21',0,'Josanvel','Jose','Velez','josanvel@espol.edu.ec',0,1,'2015-02-25 17:16:07'),(5,'pbkdf2_sha256$10000$nCppYHDdx2Y6$zvQ6/7XlFRzEhB7mRkiR9D9E2epFt1xCvT3bp/f9qvY=','2015-02-25 17:17:53',0,'uess','Universidad Espíritu Santo','','admin@correo.com',0,1,'2015-02-25 17:17:47'),(6,'pbkdf2_sha256$10000$uH9LJrGNToEP$DXFZmnFtmepG/gtvpF6RLwgysg/qTnRSAtG/9tpcxqw=','2015-02-25 17:24:50',0,'chapo','Championship Per Ordained.inc','','edisanch@espol.edu.ec',0,1,'2015-02-25 17:20:26'),(7,'pbkdf2_sha256$10000$wbQb1k4HufWm$29r4+BctWJzhwmnUsD5jjEyJfU1r3muQdEIguStYKik=','2015-02-25 17:26:08',0,'Edinson','Edinson','Sanchez','edisanch@espol.edu.ec',0,1,'2015-02-25 17:26:00'),(8,'pbkdf2_sha256$10000$ytSQvMy3khNF$G694D6xVcs4FcCLEmmIfN1kgrL67PJDRCw3GY+JIwf0=','2015-02-25 17:28:17',0,'wil','Wil','En','wil@correo.com',0,1,'2015-02-25 17:28:12'),(9,'pbkdf2_sha256$10000$IOmCcSfoSxKe$89JmAH2dcWV4wMys9F7PdI7dzZZzsYoVMPjzCOEYnng=','2015-02-25 17:29:54',0,'BRONZACHAMP','BRONZA','','alalala@gmail.com',0,1,'2015-02-25 17:29:37');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `calificacion`
--

DROP TABLE IF EXISTS `calificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `calificacion` (
  `idCalificacion` int(11) NOT NULL AUTO_INCREMENT,
  `idjurado` int(11) NOT NULL,
  `idmilestoneEntregable` int(11) NOT NULL,
  `calificacion` int(10) unsigned NOT NULL,
  `comentario` varchar(150) NOT NULL,
  PRIMARY KEY (`idCalificacion`),
  KEY `calificacion_289976e7` (`idjurado`),
  KEY `calificacion_80890d95` (`idmilestoneEntregable`),
  CONSTRAINT `idjurado_refs_idJurado_0e53b181` FOREIGN KEY (`idjurado`) REFERENCES `jurado` (`idJurado`),
  CONSTRAINT `idmilestoneEntregable_refs_idMilestoneEntregable_2abc934b` FOREIGN KEY (`idmilestoneEntregable`) REFERENCES `milestoneentregable` (`idMilestoneEntregable`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `calificacion`
--

LOCK TABLES `calificacion` WRITE;
/*!40000 ALTER TABLE `calificacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `calificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentarioDemanda`
--

DROP TABLE IF EXISTS `comentarioDemanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comentarioDemanda` (
  `idcomentario` int(11) NOT NULL AUTO_INCREMENT,
  `idDemanda` int(11) NOT NULL,
  `idpersona` int(11) NOT NULL,
  `comentario` varchar(500) NOT NULL,
  `calificacion` int(11) NOT NULL,
  PRIMARY KEY (`idcomentario`),
  KEY `comentarioDemanda_9da5d29d` (`idDemanda`),
  KEY `comentarioDemanda_88d154de` (`idpersona`),
  CONSTRAINT `idDemanda_refs_idDemanda_9e481235` FOREIGN KEY (`idDemanda`) REFERENCES `demanda` (`idDemanda`),
  CONSTRAINT `idpersona_refs_idpersona_4f07911b` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarioDemanda`
--

LOCK TABLES `comentarioDemanda` WRITE;
/*!40000 ALTER TABLE `comentarioDemanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `comentarioDemanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comentarioOferta`
--

DROP TABLE IF EXISTS `comentarioOferta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comentarioOferta` (
  `idcomentario` int(11) NOT NULL AUTO_INCREMENT,
  `idOferta` int(11) NOT NULL,
  `idpersona` int(11) NOT NULL,
  `comentario` varchar(500) NOT NULL,
  `calificacion` int(11) NOT NULL,
  `pendienteRevision` tinyint(1) NOT NULL,
  `aprobado` tinyint(1) NOT NULL,
  PRIMARY KEY (`idcomentario`),
  KEY `comentarioOferta_73e67b22` (`idOferta`),
  KEY `comentarioOferta_88d154de` (`idpersona`),
  CONSTRAINT `idpersona_refs_idpersona_7588e28f` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`),
  CONSTRAINT `idOferta_refs_idOferta_7ac867bc` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarioOferta`
--

LOCK TABLES `comentarioOferta` WRITE;
/*!40000 ALTER TABLE `comentarioOferta` DISABLE KEYS */;
/*!40000 ALTER TABLE `comentarioOferta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `concursos`
--

DROP TABLE IF EXISTS `concursos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concursos` (
  `idConcurso` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` longtext NOT NULL,
  `condiciones` longtext NOT NULL,
  `dominio` varchar(200) NOT NULL,
  `subdominio` varchar(200) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFin` date NOT NULL,
  `premios` longtext NOT NULL,
  `alcance` longtext NOT NULL,
  `num_finalistas` int(10) unsigned NOT NULL,
  `perfil` varchar(200) NOT NULL,
  `tipo_oferta` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  `ranking` int(11) NOT NULL,
  PRIMARY KEY (`idConcurso`),
  KEY `concursos_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_dd12ca56` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concursos`
--

LOCK TABLES `concursos` WRITE;
/*!40000 ALTER TABLE `concursos` DISABLE KEYS */;
INSERT INTO `concursos` VALUES (1,5,'Concurso Académico','Concurso de matemáticas','no hay condiciones','dominio','subdominio','2015-02-18','2015-02-28','Un trofeo','alcance ',2,'perfil',2,1,'conInc_media/estilo-poco-vector-libro-gordo_279-9648.jpg',0),(2,5,'Concurso de Fisica','Concurso de fisica de la universidad','resolver todos los problemas','dominio','subdominio','2015-02-27','2015-04-03','un premio','alcance',3,'perfil',1,1,'conInc_media/descarga.png',0),(3,9,'concurso1','concurso1concurso1concurso1concurso1concurso1concurso1','concurso1concurso1concurso1concurso1','concurso1concurso1concurso1concurso1','concurso1concurso1concurso1concurso1concurso1','2015-02-04','2015-02-27','concurso1concurso1concurso1concurso1concurso1','concurso1concurso1concurso1',5,'concurso1concurso1',1,1,'conInc_media/azEgE1q_700b.jpg',0);
/*!40000 ALTER TABLE `concursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `demanda`
--

DROP TABLE IF EXISTS `demanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `demanda` (
  `idDemanda` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) NOT NULL,
  `tipoDemanda` int(11) NOT NULL,
  `estadoDemanda` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `dominio` varchar(500) NOT NULL,
  `subdominio` varchar(200) NOT NULL,
  `palabras_Claves` varchar(100) NOT NULL,
  `tiempo_Inicio_Disponible` date NOT NULL,
  `tiempo_Fin_Disponible` date NOT NULL,
  `lugar_Aplicacion` varchar(200) NOT NULL,
  `perfil_Beneficiario` varchar(500) DEFAULT NULL,
  `perfil_Cliente` varchar(500) DEFAULT NULL,
  `soluciones_Alternativas` varchar(500) DEFAULT NULL,
  `importancia_Solucion` varchar(500) DEFAULT NULL,
  `imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idDemanda`),
  KEY `demanda_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_7bb72c62` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demanda`
--

LOCK TABLES `demanda` WRITE;
/*!40000 ALTER TABLE `demanda` DISABLE KEYS */;
INSERT INTO `demanda` VALUES (1,1,3,1,'kjans','kanslkas','lkasmkla','lasmlas','ñlsñla','2015-02-13','2015-02-20','13','knaslkas','lakslas','lakmsalks','añlsmkalks','ofDem_media/2013-11-25_12.35.00.jpg'),(2,4,3,1,'Spyder','jdhsakjdhsaldjlsadsadhlsdhls','1','1','araña','2015-02-02','2015-03-13','11','kjahjshadljhlfjkhkjflhewlkjfhelkjfhlkjlhjhljgljhlkj','hjlhljhlkjhlkjhlkjgkhfjgdjgfhjg','jflkjdfkjlekfjlkqefjlkefhlkjehfljewhfljwhefljwfhlkje','lkwjwedhlkewjhflkjewhflkjefhljewhfljwehfljefhlwjefhljfe','ofDem_media/spiderma.jpg'),(3,8,2,1,'Demanda UESS','demanda cualquiera','0','2','algo, algo mas, movies','2015-02-27','2015-02-28','17','perfil','perfil','descripcion','descripcion','ofDem_media/descarga_1.jpg');
/*!40000 ALTER TABLE `demanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagramacanvas`
--

DROP TABLE IF EXISTS `diagramacanvas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagramacanvas` (
  `iddiagramacanvas` int(11) NOT NULL AUTO_INCREMENT,
  `idOferta` int(11) NOT NULL,
  `redAsociados` varchar(150) DEFAULT NULL,
  `asociacionesClave` varchar(150) DEFAULT NULL,
  `actividadesClave` varchar(150) DEFAULT NULL,
  `recursosClave` varchar(150) DEFAULT NULL,
  `propuestaValor` varchar(150) DEFAULT NULL,
  `canalesDistribucion` varchar(150) DEFAULT NULL,
  `relacionClientes` varchar(150) DEFAULT NULL,
  `segmentoMercado` varchar(150) DEFAULT NULL,
  `estructuraCostos` varchar(150) DEFAULT NULL,
  `fuenteIngresos` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`iddiagramacanvas`),
  KEY `diagramacanvas_73e67b22` (`idOferta`),
  CONSTRAINT `idOferta_refs_idOferta_ebbd8cb9` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagramacanvas`
--

LOCK TABLES `diagramacanvas` WRITE;
/*!40000 ALTER TABLE `diagramacanvas` DISABLE KEYS */;
/*!40000 ALTER TABLE `diagramacanvas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagramaporter`
--

DROP TABLE IF EXISTS `diagramaporter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `diagramaporter` (
  `iddiagramaPorter` int(11) NOT NULL AUTO_INCREMENT,
  `idOferta` int(11) NOT NULL,
  `rivalidadCompetidores` varchar(200) DEFAULT NULL,
  `competidoresPotenciales` varchar(200) DEFAULT NULL,
  `proveedores` varchar(200) DEFAULT NULL,
  `sustitutos` varchar(200) DEFAULT NULL,
  `consumidores` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`iddiagramaPorter`),
  KEY `diagramaporter_73e67b22` (`idOferta`),
  CONSTRAINT `idOferta_refs_idOferta_8a09ad88` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagramaporter`
--

LOCK TABLES `diagramaporter` WRITE;
/*!40000 ALTER TABLE `diagramaporter` DISABLE KEYS */;
/*!40000 ALTER TABLE `diagramaporter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'catalogo','app','catalogo'),(8,'publicacion','app','publicacion'),(9,'concurso','concursoIncubacion','concurso'),(10,'inscripcion','concursoIncubacion','inscripcion'),(11,'milestone concurso','concursoIncubacion','milestoneconcurso'),(12,'milestone entregable','concursoIncubacion','milestoneentregable'),(13,'jurado','concursoIncubacion','jurado'),(14,'calificacion','concursoIncubacion','calificacion'),(15,'institucion','usuarios','institucion'),(16,'persona','usuarios','persona'),(17,'institucion persona','usuarios','institucionpersona'),(18,'mensaje','usuarios','mensaje'),(19,'demanda','ofertaDemanda','demanda'),(20,'comentario demanda','ofertaDemanda','comentariodemanda'),(21,'imagen demanda','ofertaDemanda','imagendemanda'),(22,'oferta','ofertaDemanda','oferta'),(23,'diagramacanvas','ofertaDemanda','diagramacanvas'),(24,'diagramaporter','ofertaDemanda','diagramaporter'),(25,'equipo','ofertaDemanda','equipo'),(26,'solicitud equipo','ofertaDemanda','solicitudequipo'),(27,'imagen oferta','ofertaDemanda','imagenoferta'),(28,'comentario oferta','ofertaDemanda','comentariooferta'),(29,'consultor','incubacion','consultor'),(30,'incubacion','incubacion','incubacion'),(31,'incubacion consultor','incubacion','incubacionconsultor'),(32,'invitacion consultor','incubacion','invitacionconsultor'),(33,'milestone','incubacion','milestone'),(34,'incubada','incubacion','incubada'),(35,'consultor incubada','incubacion','consultorincubada'),(36,'incubada milestone','incubacion','incubadamilestone'),(37,'campos adicionales milestone','incubacion','camposadicionalesmilestone'),(38,'retroalimentacion','incubacion','retroalimentacion'),(39,'convocatoria incubacion','incubacion','convocatoriaincubacion'),(40,'convocatoria incubacion ofertas','incubacion','convocatoriaincubacionofertas'),(41,'tipos ofertas incubacion','incubacion','tiposofertasincubacion');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('12nzaxl5e50rkxfoaujbzx1tesufxn2x','ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=','2015-03-11 17:33:03'),('6eljj54ypv6tx5d5qi9wphv228615snm','ODYyNTQ2YTQ2NjVkMTEzZDBhMDc2OGEzYWQ0ZTE3NWI2MWI4NzAxNjqAAn1xAShVCmlkX3BlcnNvbmFxAooBAVUHaWRfdXNlcnEDigEBVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEBVQR0aXBvcQdVB3BlcnNvbmFxCHUu','2015-03-11 17:24:05'),('hsbt9hsfyi8wkrmfc585adlwe6obh948','OGRiNDg0ZWM1YzZkNDZmOWFiYzRlY2U2NzE4ZGU4NzBjNTQwZjhjYzqAAn1xAShVCmlkX3BlcnNvbmFxAooBBVUHaWRfdXNlcnEDigEIVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEIVQR0aXBvcQdVB3BlcnNvbmFxCHUu','2015-03-11 17:28:17'),('j356uv5i1g90iwv9oex8af93fwnwrs4z','ODYyNTQ2YTQ2NjVkMTEzZDBhMDc2OGEzYWQ0ZTE3NWI2MWI4NzAxNjqAAn1xAShVCmlkX3BlcnNvbmFxAooBAVUHaWRfdXNlcnEDigEBVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEBVQR0aXBvcQdVB3BlcnNvbmFxCHUu','2015-03-11 11:29:05'),('kmnh857k1ex237jhg4p6xzro8x112foi','NGZmMGIwOTc3MDlhOTM5MGFiMjJlMGZlZDE3OGFkNjg2YzJjODExMTqAAn1xAShVCmlkX3BlcnNvbmFxAooBBFUHaWRfdXNlcnEDigEHVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEHVQR0aXBvcQdVB3BlcnNvbmFxCHUu','2015-03-11 17:26:08'),('o07nv0agatb23lu24swrnp3mb6a0tarp','MjgzMDNlZDViYmE5ZTg5MGVhOGE5MGFiMTAyOWZlMmFjZDMxMDk4MjqAAn1xAShVCmlkX3BlcnNvbmFxAooBA1UHaWRfdXNlcnEDigEEVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEEVQR0aXBvcQdVB3BlcnNvbmFxCHUu','2015-03-11 17:16:21'),('oxdthcmhyco3fx6zla23l6sp4jz54plf','ODYyNTQ2YTQ2NjVkMTEzZDBhMDc2OGEzYWQ0ZTE3NWI2MWI4NzAxNjqAAn1xAShVCmlkX3BlcnNvbmFxAooBAVUHaWRfdXNlcnEDigEBVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEBVQR0aXBvcQdVB3BlcnNvbmFxCHUu','2015-03-11 09:45:05'),('y6kmytn5349lcp8tppimhmn3os7eba4n','MjgxODYyOGMxN2UwODc4NDUwNDk5NWRmZjY0YjhhMDI3ZDFiZDVjNDqAAn1xAShVDmlkX2luc3RpdHVjaW9ucQKKAQFVB2lkX3VzZXJxA4oBAlUSX2F1dGhfdXNlcl9iYWNrZW5kcQRVKWRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kcQVVDV9hdXRoX3VzZXJfaWRxBooBAlUEdGlwb3EHVQtpbnN0aXR1Y2lvbnEIdS4=','2015-03-11 09:55:05');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipo`
--

DROP TABLE IF EXISTS `equipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipo` (
  `idequipo` int(11) NOT NULL AUTO_INCREMENT,
  `idOferta` int(11) NOT NULL,
  `idpersona` int(11) NOT NULL,
  `rol` varchar(100) NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`idequipo`),
  KEY `equipo_54319a0f` (`idOferta`),
  KEY `equipo_88d154de` (`idpersona`),
  CONSTRAINT `idpersona_refs_idpersona_5f95a377` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`),
  CONSTRAINT `idOferta_refs_idOferta_e4728d4a` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipo`
--

LOCK TABLES `equipo` WRITE;
/*!40000 ALTER TABLE `equipo` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagenDemanda`
--

DROP TABLE IF EXISTS `imagenDemanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imagenDemanda` (
  `idimagen` int(11) NOT NULL AUTO_INCREMENT,
  `idDemanda` int(11) NOT NULL,
  `enlace_imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idimagen`),
  KEY `imagenDemanda_9da5d29d` (`idDemanda`),
  CONSTRAINT `idDemanda_refs_idDemanda_71bc5e61` FOREIGN KEY (`idDemanda`) REFERENCES `demanda` (`idDemanda`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagenDemanda`
--

LOCK TABLES `imagenDemanda` WRITE;
/*!40000 ALTER TABLE `imagenDemanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `imagenDemanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `imagenOferta`
--

DROP TABLE IF EXISTS `imagenOferta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `imagenOferta` (
  `idimagen` int(11) NOT NULL AUTO_INCREMENT,
  `idOferta` int(11) NOT NULL,
  `enlace_imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idimagen`),
  KEY `imagenOferta_73e67b22` (`idOferta`),
  CONSTRAINT `idOferta_refs_idOferta_887f9dd9` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `imagenOferta`
--

LOCK TABLES `imagenOferta` WRITE;
/*!40000 ALTER TABLE `imagenOferta` DISABLE KEYS */;
/*!40000 ALTER TABLE `imagenOferta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inscripcion`
--

DROP TABLE IF EXISTS `inscripcion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inscripcion` (
  `idInscripcion` int(11) NOT NULL AUTO_INCREMENT,
  `idconcurso` int(11) NOT NULL,
  `idoferta` int(11) NOT NULL,
  `fechainscripcion` date NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`idInscripcion`),
  KEY `inscripcion_a5f36d76` (`idconcurso`),
  KEY `inscripcion_73e67b22` (`idoferta`),
  CONSTRAINT `idoferta_refs_idOferta_55fda789` FOREIGN KEY (`idoferta`) REFERENCES `oferta` (`idOferta`),
  CONSTRAINT `idconcurso_refs_idConcurso_65b459d0` FOREIGN KEY (`idconcurso`) REFERENCES `concursos` (`idConcurso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inscripcion`
--

LOCK TABLES `inscripcion` WRITE;
/*!40000 ALTER TABLE `inscripcion` DISABLE KEYS */;
/*!40000 ALTER TABLE `inscripcion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institucion`
--

DROP TABLE IF EXISTS `institucion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institucion` (
  `user_ptr_id` int(11) NOT NULL,
  `idinstitucion` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_corto` varchar(20) NOT NULL,
  `descripcion` varchar(900) NOT NULL,
  `mision` varchar(900) NOT NULL,
  `sitio_web` varchar(200) NOT NULL,
  `persona_que_registra` varchar(200) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `recursos` varchar(100) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idinstitucion`),
  UNIQUE KEY `user_ptr_id` (`user_ptr_id`),
  CONSTRAINT `user_ptr_id_refs_id_fd310a34` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institucion`
--

LOCK TABLES `institucion` WRITE;
/*!40000 ALTER TABLE `institucion` DISABLE KEYS */;
INSERT INTO `institucion` VALUES (2,1,'ñalskñal','asñlañsl','sñalmasñ','añlsmas','sañslmasñl','añlksañs','añslalñs','usuarios_media/laberinto3.jpg'),(5,2,'UESS','universidad','Educar','uess@daw.com','admin','123123','recursos','usuarios_media/pes2013-ronaldo_03.jpg'),(6,3,'CHAPO .inc','corporacion de manejo , compra y venta de bienes raices con fines de lucro','Hacer billete','www.CHAPO.com','chapo','09971779999','bienes raices','usuarios_media/CHAPY-PC_-_WIN_20141001_105924.JPG'),(9,4,'asojdbqwsudbnasjl/kd','oi\'asnd\'iqdwnasljkd','o\'lansd\'qwuodbasljk','\'douasbda\'osudbasjl/m','ouasjbdauso\'dbasojl\'','2822406','akjsdjlaso;idn','usuarios_media/espol.png');
/*!40000 ALTER TABLE `institucion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `institucion_persona`
--

DROP TABLE IF EXISTS `institucion_persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `institucion_persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idpersona` int(11) NOT NULL,
  `idinstitucion` int(11) NOT NULL,
  `cargoPersona` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `institucion_persona_8adb2a44` (`idpersona`),
  KEY `institucion_persona_a6094bcf` (`idinstitucion`),
  CONSTRAINT `idinstitucion_refs_idinstitucion_b1def11b` FOREIGN KEY (`idinstitucion`) REFERENCES `institucion` (`idinstitucion`),
  CONSTRAINT `idpersona_refs_idpersona_471c0464` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institucion_persona`
--

LOCK TABLES `institucion_persona` WRITE;
/*!40000 ALTER TABLE `institucion_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `institucion_persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jurado`
--

DROP TABLE IF EXISTS `jurado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jurado` (
  `idJurado` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) NOT NULL,
  `idConcurso` int(11) NOT NULL,
  PRIMARY KEY (`idJurado`),
  KEY `jurado_88d154de` (`idusuario`),
  KEY `jurado_a5f36d76` (`idConcurso`),
  CONSTRAINT `idusuario_refs_id_f748087b` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `idConcurso_refs_idConcurso_28848497` FOREIGN KEY (`idConcurso`) REFERENCES `concursos` (`idConcurso`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jurado`
--

LOCK TABLES `jurado` WRITE;
/*!40000 ALTER TABLE `jurado` DISABLE KEYS */;
/*!40000 ALTER TABLE `jurado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensaje`
--

DROP TABLE IF EXISTS `mensaje`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mensaje` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `idp_emisor` int(11) NOT NULL,
  `idp_destino` int(11) NOT NULL,
  `asunto` varchar(50) NOT NULL,
  `txtMensaje` longtext NOT NULL,
  `fecha` date NOT NULL,
  `hora` time NOT NULL,
  `leido` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mensaje_f28dad41` (`idp_emisor`),
  KEY `mensaje_12cc1b67` (`idp_destino`),
  CONSTRAINT `idp_destino_refs_id_d80e1931` FOREIGN KEY (`idp_destino`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `idp_emisor_refs_id_d80e1931` FOREIGN KEY (`idp_emisor`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensaje`
--

LOCK TABLES `mensaje` WRITE;
/*!40000 ALTER TABLE `mensaje` DISABLE KEYS */;
INSERT INTO `mensaje` VALUES (1,2,1,'Asuntoqwerf','rdfgyhujkl','2012-12-12','12:00:00',1),(2,1,2,'Clase','Quiero clases','2012-12-12','12:00:00',1),(3,1,2,'Clase','Quiero clases','2012-12-12','12:00:00',1),(4,1,2,'kjas','akbjsas','2015-02-25','12:00:00',1),(5,1,2,'Asuntoqwerf','JAJA','2015-02-25','12:00:00',1),(6,5,2,'Mensaje de prueba','Este es un mensaje de prueba','2015-02-25','12:00:00',1),(7,7,1,'pilas mensaje de prueba','este es un mensaje de prueba avisa cualquiercosa','2015-02-25','12:00:00',1),(8,4,3,'sdkfskjdfkjfkdjflk','dlajvñldjfñlkjdsvñlkdjfñlksdjfñlkdjfñljsñ,josejñkskskl','2015-02-25','12:00:00',1),(9,7,3,'pilas fausto','mensaje de prueba','2015-02-25','12:00:00',1),(10,4,7,'lkssjdhflkjdhfkjlh','lkajdlkjdflkenflkj','2015-02-25','12:00:00',1),(11,4,6,'.,jdfndsnfmdsn.,m','s.dkvjslkvn.dvn.kdnvkdnvljdsnvlkjjdsnvlkjdvdsv','2015-02-25','12:00:00',1);
/*!40000 ALTER TABLE `mensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `milestoneConcurso`
--

DROP TABLE IF EXISTS `milestoneConcurso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `milestoneConcurso` (
  `idMilestone` int(11) NOT NULL AUTO_INCREMENT,
  `idConcurso` int(11) NOT NULL,
  `fecha_entrega` date NOT NULL,
  `requerimiento` varchar(300) NOT NULL,
  `peso` int(10) unsigned NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`idMilestone`),
  KEY `milestoneConcurso_a5f36d76` (`idConcurso`),
  CONSTRAINT `idConcurso_refs_idConcurso_5089d1ce` FOREIGN KEY (`idConcurso`) REFERENCES `concursos` (`idConcurso`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `milestoneConcurso`
--

LOCK TABLES `milestoneConcurso` WRITE;
/*!40000 ALTER TABLE `milestoneConcurso` DISABLE KEYS */;
INSERT INTO `milestoneConcurso` VALUES (1,1,'2015-02-07','Ganar el concurso',1,1),(2,2,'2015-02-14','milestone x',3,1),(3,3,'2015-02-27','concurso1concurso1',16,1),(4,3,'2015-02-28','concurso1concurso1concurso1',17,1);
/*!40000 ALTER TABLE `milestoneConcurso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `milestoneentregable`
--

DROP TABLE IF EXISTS `milestoneentregable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `milestoneentregable` (
  `idMilestoneEntregable` int(11) NOT NULL AUTO_INCREMENT,
  `idmilestoneConcurso` int(11) NOT NULL,
  `idinscripcion` int(11) NOT NULL,
  `fecha_entrega` date NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`idMilestoneEntregable`),
  KEY `milestoneentregable_89bd017b` (`idmilestoneConcurso`),
  KEY `milestoneentregable_f2bedb5f` (`idinscripcion`),
  CONSTRAINT `idinscripcion_refs_idInscripcion_8a8f7d01` FOREIGN KEY (`idinscripcion`) REFERENCES `inscripcion` (`idInscripcion`),
  CONSTRAINT `idmilestoneConcurso_refs_idMilestone_278d5d59` FOREIGN KEY (`idmilestoneConcurso`) REFERENCES `milestoneConcurso` (`idMilestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `milestoneentregable`
--

LOCK TABLES `milestoneentregable` WRITE;
/*!40000 ALTER TABLE `milestoneentregable` DISABLE KEYS */;
/*!40000 ALTER TABLE `milestoneentregable` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oferta`
--

DROP TABLE IF EXISTS `oferta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oferta` (
  `idOferta` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) NOT NULL,
  `tipoOferta` int(11) NOT NULL,
  `estadoOferta` int(11) NOT NULL,
  `calificacionGeneral` int(11) DEFAULT NULL,
  `ofertaPublicada` tinyint(1) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `dominio` varchar(500) NOT NULL,
  `subdominio` varchar(200) NOT NULL,
  `palabras_Claves` varchar(200) NOT NULL,
  `tiempo_Inicio_Disponible` date NOT NULL,
  `tiempo_Fin_Disponible` date NOT NULL,
  `lugar_Aplicacion` varchar(200) NOT NULL,
  `perfil_Beneficiario` varchar(500) DEFAULT NULL,
  `perfil_Cliente` varchar(500) DEFAULT NULL,
  `soluciones_Alternativas` varchar(500) DEFAULT NULL,
  `propuesta_Valor` varchar(300) DEFAULT NULL,
  `cuadro_Competidores` varchar(500) DEFAULT NULL,
  `cuadro_Tendencias_Relevantes` varchar(500) DEFAULT NULL,
  `estado_Propiedad_Intelectual` varchar(500) DEFAULT NULL,
  `evidencia_Traccion` varchar(500) DEFAULT NULL,
  `imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idOferta`),
  KEY `oferta_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_19f5410d` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oferta`
--

LOCK TABLES `oferta` WRITE;
/*!40000 ALTER TABLE `oferta` DISABLE KEYS */;
INSERT INTO `oferta` VALUES (1,1,1,1,NULL,1,'lkasmas','lasmlask','lakmslka','lkasmlas','alsmñlas','2015-02-04','2015-02-12','1','lknkl','lkjlk','lklkñ','lkñkl','','','','lij','ofDem_media/2013-11-25_12.35.00_1.jpg'),(2,3,1,1,NULL,1,'BRONZAAAA','lalalalalalalala allalalalalalaa alallaamskdausdasjlk/dasnldkjn ','aklsdnasohidu;bn\'','lajsbdou\'qbd\'ouaj','auosbdou\'asdbuso\'a','2015-02-12','2015-02-28','1','kasndpiqwndLASbdljj','ljabsdluoqwjbdlubasnLJD','pibnv\'WIBODFL\'wefn\'ilWDFNIL','J\'LASND\'IOQWND\'I','','','','\'OLASNDPIQWNDPIQWNDOWI\'BND','ofDem_media/azEgE1q_700b.jpg'),(3,4,2,1,NULL,1,'Dota2','jhsbdhjsLDKJHSLDJhslkdhslahjl','lfaffdhldhjsflkhflkkdhflkjj','vlkkadhvlkdslshjd','lhaslvhaldvhl','2015-02-02','2015-02-03','5','asnf.dsn.,NMD','SKJHFKDSJHFLJLF','skdjfdkjfndkjfkj','jfkljdflkjdk.','','','','jkhflkjlfkj','ofDem_media/razor.jpg'),(4,8,1,1,NULL,1,'Oferta de Trabajo','Se busca trabajador para construccion','dominio','subdominio','trabajo, construcciones','2015-02-02','2015-02-21','20','un beneficiario','un cliente','soluciones','alguna propuesta','','','','evidencias','ofDem_media/5177_icon.png');
/*!40000 ALTER TABLE `oferta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `persona` (
  `user_ptr_id` int(11) NOT NULL,
  `idpersona` int(11) NOT NULL AUTO_INCREMENT,
  `identificacion` varchar(20) NOT NULL,
  `cargo` varchar(50) NOT NULL,
  `actividad` varchar(150) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `areas_interes` varchar(50) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idpersona`),
  UNIQUE KEY `user_ptr_id` (`user_ptr_id`),
  CONSTRAINT `user_ptr_id_refs_id_378c361a` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,1,'18726812','Los cargos','Muchas actividades','2012-12-12','Pocas','usuarios_media/2013-11-25_12.35.00.jpg'),(3,2,'9839859284','aallaalall','allalalal','2012-12-12','alalalalal','usuarios_media/caesar.jpg'),(4,3,'930566666','Estudiante','Estudiar','2012-12-12','Tecnologia','usuarios_media/razor.jpg'),(7,4,'123456789','supervisor','Estudiante','2012-12-12','Computacion','usuarios_media/download_1.jpg'),(8,5,'91239123','estudiante','actividades','2012-12-12','estudiar','usuarios_media/descarga.jpg');
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publicacion`
--

DROP TABLE IF EXISTS `publicacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `publicacion` (
  `idpublicacion` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `dominio` varchar(200) NOT NULL,
  `subdominio` varchar(200) NOT NULL,
  PRIMARY KEY (`idpublicacion`),
  KEY `publicacion_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_fcdc7503` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publicacion`
--

LOCK TABLES `publicacion` WRITE;
/*!40000 ALTER TABLE `publicacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `publicacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `solicitudEquipo`
--

DROP TABLE IF EXISTS `solicitudEquipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `solicitudEquipo` (
  `idSolicitudEquipo` int(11) NOT NULL AUTO_INCREMENT,
  `idequipo` int(11) NOT NULL,
  `idpersona` int(11) NOT NULL,
  `pendienteRevision` tinyint(1) NOT NULL,
  `aprobada` tinyint(1) NOT NULL,
  PRIMARY KEY (`idSolicitudEquipo`),
  KEY `solicitudEquipo_05b7cb86` (`idequipo`),
  KEY `solicitudEquipo_88d154de` (`idpersona`),
  CONSTRAINT `idpersona_refs_idpersona_b50a17a3` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`),
  CONSTRAINT `idequipo_refs_idequipo_6e982415` FOREIGN KEY (`idequipo`) REFERENCES `equipo` (`idequipo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitudEquipo`
--

LOCK TABLES `solicitudEquipo` WRITE;
/*!40000 ALTER TABLE `solicitudEquipo` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitudEquipo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-02-25 12:40:18
