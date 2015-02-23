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
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add publicacion',7,'add_publicacion'),(20,'Can change publicacion',7,'change_publicacion'),(21,'Can delete publicacion',7,'delete_publicacion'),(22,'Can add concurso',8,'add_concurso'),(23,'Can change concurso',8,'change_concurso'),(24,'Can delete concurso',8,'delete_concurso'),(25,'Can add incubacion',9,'add_incubacion'),(26,'Can change incubacion',9,'change_incubacion'),(27,'Can delete incubacion',9,'delete_incubacion'),(28,'Can add solicitud',10,'add_solicitud'),(29,'Can change solicitud',10,'change_solicitud'),(30,'Can delete solicitud',10,'delete_solicitud'),(31,'Can add milestone',11,'add_milestone'),(32,'Can change milestone',11,'change_milestone'),(33,'Can delete milestone',11,'delete_milestone'),(34,'Can add milestone participante',12,'add_milestoneparticipante'),(35,'Can change milestone participante',12,'change_milestoneparticipante'),(36,'Can delete milestone participante',12,'delete_milestoneparticipante'),(37,'Can add convocatoria',13,'add_convocatoria'),(38,'Can change convocatoria',13,'change_convocatoria'),(39,'Can delete convocatoria',13,'delete_convocatoria'),(40,'Can add institucion',14,'add_institucion'),(41,'Can change institucion',14,'change_institucion'),(42,'Can delete institucion',14,'delete_institucion'),(43,'Can add institucion persona',15,'add_institucionpersona'),(44,'Can change institucion persona',15,'change_institucionpersona'),(45,'Can delete institucion persona',15,'delete_institucionpersona'),(46,'Can add persona',16,'add_persona'),(47,'Can change persona',16,'change_persona'),(48,'Can delete persona',16,'delete_persona'),(49,'Can add mensaje',17,'add_mensaje'),(50,'Can change mensaje',17,'change_mensaje'),(51,'Can delete mensaje',17,'delete_mensaje'),(52,'Can add demanda',18,'add_demanda'),(53,'Can change demanda',18,'change_demanda'),(54,'Can delete demanda',18,'delete_demanda'),(55,'Can add comentario demanda',19,'add_comentariodemanda'),(56,'Can change comentario demanda',19,'change_comentariodemanda'),(57,'Can delete comentario demanda',19,'delete_comentariodemanda'),(58,'Can add imagen demanda',20,'add_imagendemanda'),(59,'Can change imagen demanda',20,'change_imagendemanda'),(60,'Can delete imagen demanda',20,'delete_imagendemanda'),(61,'Can add oferta',21,'add_oferta'),(62,'Can change oferta',21,'change_oferta'),(63,'Can delete oferta',21,'delete_oferta'),(64,'Can add diagramacanvas',22,'add_diagramacanvas'),(65,'Can change diagramacanvas',22,'change_diagramacanvas'),(66,'Can delete diagramacanvas',22,'delete_diagramacanvas'),(67,'Can add diagramaporter',23,'add_diagramaporter'),(68,'Can change diagramaporter',23,'change_diagramaporter'),(69,'Can delete diagramaporter',23,'delete_diagramaporter'),(70,'Can add equipo',24,'add_equipo'),(71,'Can change equipo',24,'change_equipo'),(72,'Can delete equipo',24,'delete_equipo'),(73,'Can add solicitud equipo',25,'add_solicitudequipo'),(74,'Can change solicitud equipo',25,'change_solicitudequipo'),(75,'Can delete solicitud equipo',25,'delete_solicitudequipo'),(76,'Can add imagen oferta',26,'add_imagenoferta'),(77,'Can change imagen oferta',26,'change_imagenoferta'),(78,'Can delete imagen oferta',26,'delete_imagenoferta'),(79,'Can add comentario oferta',27,'add_comentariooferta'),(80,'Can change comentario oferta',27,'change_comentariooferta'),(81,'Can delete comentario oferta',27,'delete_comentariooferta');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$xlYL09Pt1EWX$mE7SVF/WfTvVOoEXX/mQ4Qa/GnAKc26s/HeDKlenTkQ=','2015-02-22 20:10:46',0,'xngelguale','Angel','Guale','xngelguale@yahoo.com',0,1,'2015-02-22 09:41:00'),(2,'pbkdf2_sha256$10000$CW0MbmjwhF3z$4ZqW3yHvigb3nyUc6VsNFlNxpd87BVTN109WeWEZRjM=','2015-02-22 19:42:55',0,'adguale','Angel','Guale','xngelguale@yahoo.com',0,1,'2015-02-22 18:16:53'),(3,'pbkdf2_sha256$10000$WlXUFJz9F4e3$OtSI2p8LD4LjhmwvtXSiE871WVzDRqahOxigmDRlf08=','2015-02-22 20:04:21',0,'adguale11','Angel','Guale Lainez','xngelguale@yahoo.com',0,1,'2015-02-22 19:50:19'),(4,'pbkdf2_sha256$10000$FuSRnm0lJFz1$Bq2O9ZOvCKetl5/oBu7M9JyoFhYthS38/VnfcUG9/BU=','2015-02-22 21:41:43',0,'temp','Angel','Guale Lainez','xngelguale@yahoo.com',0,1,'2015-02-22 21:41:35');
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
  CONSTRAINT `idOferta_refs_idOferta_7ac867bc` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`),
  CONSTRAINT `idpersona_refs_idpersona_7588e28f` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`)
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
  `descripcion` varchar(500) NOT NULL,
  `dominio` varchar(200) NOT NULL,
  `subdominio` varchar(200) NOT NULL,
  `fechaInicio` date NOT NULL,
  `fechaFin` date NOT NULL,
  `premios` varchar(200) NOT NULL,
  `alcance` varchar(300) NOT NULL,
  `num_finalistas` int(11) NOT NULL,
  `perfil` varchar(200) NOT NULL,
  `tipo_oferta` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idConcurso`),
  KEY `concursos_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_dd12ca56` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concursos`
--

LOCK TABLES `concursos` WRITE;
/*!40000 ALTER TABLE `concursos` DISABLE KEYS */;
/*!40000 ALTER TABLE `concursos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `convocatoria`
--

DROP TABLE IF EXISTS `convocatoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `convocatoria` (
  `idConvocatoria` int(11) NOT NULL AUTO_INCREMENT,
  `fechaInicio` date NOT NULL,
  `fechaFin` date NOT NULL,
  `idpublicacionConvocatoria` int(11) NOT NULL,
  PRIMARY KEY (`idConvocatoria`),
  KEY `convocatoria_f6eeb65f` (`idpublicacionConvocatoria`),
  CONSTRAINT `idpublicacionConvocatoria_refs_idpublicacion_bc2881b6` FOREIGN KEY (`idpublicacionConvocatoria`) REFERENCES `publicacion` (`idpublicacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `convocatoria`
--

LOCK TABLES `convocatoria` WRITE;
/*!40000 ALTER TABLE `convocatoria` DISABLE KEYS */;
/*!40000 ALTER TABLE `convocatoria` ENABLE KEYS */;
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
  `dominio` int(11) NOT NULL,
  `subdominio` int(11) NOT NULL,
  `palabras_Claves` varchar(100) NOT NULL,
  `tiempo_Inicio_Disponible` date NOT NULL,
  `tiempo_Fin_Disponible` date NOT NULL,
  `lugar_Aplicacion` varchar(200) NOT NULL,
  `perfil_Beneficiario` varchar(500) DEFAULT NULL,
  `perfil_Cliente` varchar(500) DEFAULT NULL,
  `soluciones_Alternativas` varchar(500) DEFAULT NULL,
  `importancia_Solucion` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`idDemanda`),
  KEY `demanda_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_7bb72c62` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demanda`
--

LOCK TABLES `demanda` WRITE;
/*!40000 ALTER TABLE `demanda` DISABLE KEYS */;
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
  `asociacionesClave` varchar(150) DEFAULT NULL,
  `actividadesClave` varchar(150) DEFAULT NULL,
  `recursosClave` varchar(150) DEFAULT NULL,
  `propuestaValor` varchar(150) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'publicacion','app','publicacion'),(8,'concurso','concursoIncubacion','concurso'),(9,'incubacion','concursoIncubacion','incubacion'),(10,'solicitud','concursoIncubacion','solicitud'),(11,'milestone','concursoIncubacion','milestone'),(12,'milestone participante','concursoIncubacion','milestoneparticipante'),(13,'convocatoria','concursoIncubacion','convocatoria'),(14,'institucion','usuarios','institucion'),(15,'institucion persona','usuarios','institucionpersona'),(16,'persona','usuarios','persona'),(17,'mensaje','usuarios','mensaje'),(18,'demanda','ofertaDemanda','demanda'),(19,'comentario demanda','ofertaDemanda','comentariodemanda'),(20,'imagen demanda','ofertaDemanda','imagendemanda'),(21,'oferta','ofertaDemanda','oferta'),(22,'diagramacanvas','ofertaDemanda','diagramacanvas'),(23,'diagramaporter','ofertaDemanda','diagramaporter'),(24,'equipo','ofertaDemanda','equipo'),(25,'solicitud equipo','ofertaDemanda','solicitudequipo'),(26,'imagen oferta','ofertaDemanda','imagenoferta'),(27,'comentario oferta','ofertaDemanda','comentariooferta');
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
INSERT INTO `django_session` VALUES ('19p422kb0jyvpgi2yw2z22t3uyctf25e','ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=','2015-03-08 19:58:31'),('7i65754ts8l1sdr24tpvnfzp8bt558da','ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=','2015-03-08 20:01:54'),('98qqvy8is9rrigluqm235r64p34d9j7k','ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=','2015-03-08 20:03:38'),('cx3ve0se4f8yvs595ac4ocqtg3lp1dgm','ZGIzNGIwOGU4YTI3NjYzZmY4OTZhMDMyZTI3NWI1MjVhNzQwYTk3YzqAAn1xAShVCmlkX3BlcnNvbmFxAooBBFUHaWRfdXNlcnEDigEEVRJfYXV0aF91c2VyX2JhY2tlbmRxBFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxBVUNX2F1dGhfdXNlcl9pZHEGigEEdS4=','2015-03-08 21:41:43'),('n6ep659755ofxci41neak8qxwct8k03b','ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=','2015-03-08 19:59:25'),('wt68vp8oj08ua8u6hwcsqe0hfcmewl38','ODdmNTA3M2M4YTc1MWIwMTI4M2E1ZGViOTA2YzJhY2ZjZmFiNGNhMzqAAn1xAS4=','2015-03-08 19:59:45');
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
  CONSTRAINT `idOferta_refs_idOferta_e4728d4a` FOREIGN KEY (`idOferta`) REFERENCES `oferta` (`idOferta`),
  CONSTRAINT `idpersona_refs_idpersona_5f95a377` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`)
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
-- Table structure for table `incubacion`
--

DROP TABLE IF EXISTS `incubacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `incubacion` (
  `idDetalleIncubacion` int(11) NOT NULL AUTO_INCREMENT,
  `idusuario` int(11) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `dominio` varchar(200) NOT NULL,
  `subdominio` varchar(200) NOT NULL,
  `fechaInicio` date NOT NULL,
  `condiciones` varchar(300) NOT NULL,
  `perfil_oferta` varchar(200) NOT NULL,
  `tipo_oferta` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  `imagen` varchar(100) NOT NULL,
  PRIMARY KEY (`idDetalleIncubacion`),
  KEY `incubacion_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_45b07ba9` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incubacion`
--

LOCK TABLES `incubacion` WRITE;
/*!40000 ALTER TABLE `incubacion` DISABLE KEYS */;
/*!40000 ALTER TABLE `incubacion` ENABLE KEYS */;
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
  `idAdministrador` int(11) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `recursos` varchar(100) NOT NULL,
  PRIMARY KEY (`idinstitucion`),
  UNIQUE KEY `user_ptr_id` (`user_ptr_id`),
  CONSTRAINT `user_ptr_id_refs_id_fd310a34` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `institucion`
--

LOCK TABLES `institucion` WRITE;
/*!40000 ALTER TABLE `institucion` DISABLE KEYS */;
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
  CONSTRAINT `idpersona_refs_idpersona_471c0464` FOREIGN KEY (`idpersona`) REFERENCES `persona` (`idpersona`),
  CONSTRAINT `idinstitucion_refs_idinstitucion_b1def11b` FOREIGN KEY (`idinstitucion`) REFERENCES `institucion` (`idinstitucion`)
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensaje`
--

LOCK TABLES `mensaje` WRITE;
/*!40000 ALTER TABLE `mensaje` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensaje` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `milestone`
--

DROP TABLE IF EXISTS `milestone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `milestone` (
  `idMilestone` int(11) NOT NULL AUTO_INCREMENT,
  `idpublicacion` int(11) NOT NULL,
  `fecha_entrega` date NOT NULL,
  `requerimiento` varchar(300) NOT NULL,
  `campo_nuevo` varchar(300) NOT NULL,
  `peso` int(11) NOT NULL,
  `calificacion` int(11) DEFAULT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`idMilestone`),
  KEY `milestone_5232bf5a` (`idpublicacion`),
  CONSTRAINT `idpublicacion_refs_idpublicacion_68e2b755` FOREIGN KEY (`idpublicacion`) REFERENCES `publicacion` (`idpublicacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `milestone`
--

LOCK TABLES `milestone` WRITE;
/*!40000 ALTER TABLE `milestone` DISABLE KEYS */;
/*!40000 ALTER TABLE `milestone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `milestoneparticipante`
--

DROP TABLE IF EXISTS `milestoneparticipante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `milestoneparticipante` (
  `idMilestoneparticipante` int(11) NOT NULL AUTO_INCREMENT,
  `idmilestone` int(11) NOT NULL,
  `idsolicitud` int(11) NOT NULL,
  PRIMARY KEY (`idMilestoneparticipante`),
  KEY `milestoneparticipante_5df947ef` (`idmilestone`),
  KEY `milestoneparticipante_46fc8fcc` (`idsolicitud`),
  CONSTRAINT `idsolicitud_refs_idsolicitud_abc008a4` FOREIGN KEY (`idsolicitud`) REFERENCES `solicitud` (`idsolicitud`),
  CONSTRAINT `idmilestone_refs_idMilestone_805c68fd` FOREIGN KEY (`idmilestone`) REFERENCES `milestone` (`idMilestone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `milestoneparticipante`
--

LOCK TABLES `milestoneparticipante` WRITE;
/*!40000 ALTER TABLE `milestoneparticipante` DISABLE KEYS */;
/*!40000 ALTER TABLE `milestoneparticipante` ENABLE KEYS */;
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
  `cuadro_Competidores` varchar(100) DEFAULT NULL,
  `cuadro_Tendencias_Relevantes` varchar(100) DEFAULT NULL,
  `estado_Propiedad_Intelectual` varchar(500) DEFAULT NULL,
  `evidencia_Traccion` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`idOferta`),
  KEY `oferta_88d154de` (`idusuario`),
  CONSTRAINT `idusuario_refs_id_19f5410d` FOREIGN KEY (`idusuario`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oferta`
--

LOCK TABLES `oferta` WRITE;
/*!40000 ALTER TABLE `oferta` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,1,'1256789','das','afasd','2012-12-12','Matematicas y Ajedrez','usuarios_media/Christmas_Grinch.jpg'),(2,2,'123','Los cargos','alksals','2012-12-12','alkslas','usuarios_media/jesus_mundial.jpg'),(3,3,'123455','lkans','alksals','2012-12-12','Pocas',''),(4,4,'1982718932','Los cargos','Muchas actividades','2012-12-12','Matematicas y Ajedrez','usuarios_media/Grinch3.jpg');
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
-- Table structure for table `solicitud`
--

DROP TABLE IF EXISTS `solicitud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `solicitud` (
  `idsolicitud` int(11) NOT NULL AUTO_INCREMENT,
  `idpublicacion` int(11) NOT NULL,
  `idofertapublicada` int(11) NOT NULL,
  `fechaSol` date NOT NULL,
  PRIMARY KEY (`idsolicitud`),
  KEY `solicitud_ed226d30` (`idpublicacion`),
  KEY `solicitud_69410e7c` (`idofertapublicada`),
  CONSTRAINT `idofertapublicada_refs_idpublicacion_08615910` FOREIGN KEY (`idofertapublicada`) REFERENCES `publicacion` (`idpublicacion`),
  CONSTRAINT `idpublicacion_refs_idpublicacion_08615910` FOREIGN KEY (`idpublicacion`) REFERENCES `publicacion` (`idpublicacion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `solicitud`
--

LOCK TABLES `solicitud` WRITE;
/*!40000 ALTER TABLE `solicitud` DISABLE KEYS */;
/*!40000 ALTER TABLE `solicitud` ENABLE KEYS */;
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

-- Dump completed on 2015-02-22 17:32:19
