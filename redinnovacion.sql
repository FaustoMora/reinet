-- MySQL Script generated by MySQL Workbench
-- 02/21/15 22:38:22
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema redinnovacion
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema redinnovacion
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `redinnovacion` DEFAULT CHARACTER SET utf8 ;
USE `redinnovacion` ;

-- -----------------------------------------------------
-- Table `redinnovacion`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`auth_group` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`django_content_type` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `app_label` (`app_label` ASC, `model` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 28
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`auth_permission` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  `content_type_id` INT(11) NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `content_type_id` (`content_type_id` ASC, `codename` ASC),
  INDEX `auth_permission_37ef4eb4` (`content_type_id` ASC),
  CONSTRAINT `content_type_id_refs_id_d043b34a`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `redinnovacion`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 82
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`auth_group_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `group_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `group_id` (`group_id` ASC, `permission_id` ASC),
  INDEX `auth_group_permissions_5f412f9a` (`group_id` ASC),
  INDEX `auth_group_permissions_83d7f98b` (`permission_id` ASC),
  CONSTRAINT `group_id_refs_id_f4b32aac`
    FOREIGN KEY (`group_id`)
    REFERENCES `redinnovacion`.`auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519`
    FOREIGN KEY (`permission_id`)
    REFERENCES `redinnovacion`.`auth_permission` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`auth_user` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME NOT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(30) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(30) NOT NULL,
  `email` VARCHAR(75) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`auth_user_groups` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `group_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id` (`user_id` ASC, `group_id` ASC),
  INDEX `auth_user_groups_6340c63c` (`user_id` ASC),
  INDEX `auth_user_groups_5f412f9a` (`group_id` ASC),
  CONSTRAINT `group_id_refs_id_274b862c`
    FOREIGN KEY (`group_id`)
    REFERENCES `redinnovacion`.`auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112`
    FOREIGN KEY (`user_id`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`auth_user_user_permissions` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `permission_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `user_id` (`user_id` ASC, `permission_id` ASC),
  INDEX `auth_user_user_permissions_6340c63c` (`user_id` ASC),
  INDEX `auth_user_user_permissions_83d7f98b` (`permission_id` ASC),
  CONSTRAINT `permission_id_refs_id_35d9ac25`
    FOREIGN KEY (`permission_id`)
    REFERENCES `redinnovacion`.`auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39`
    FOREIGN KEY (`user_id`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`demanda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`demanda` (
  `idDemanda` INT(11) NOT NULL AUTO_INCREMENT,
  `idusuario` INT(11) NOT NULL,
  `tipoDemanda` INT(11) NOT NULL,
  `estadoDemanda` INT(11) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  `dominio` INT(11) NOT NULL,
  `subdominio` INT(11) NOT NULL,
  `palabras_Claves` VARCHAR(100) NOT NULL,
  `tiempo_Inicio_Disponible` DATE NOT NULL,
  `tiempo_Fin_Disponible` DATE NOT NULL,
  `lugar_Aplicacion` VARCHAR(200) NOT NULL,
  `perfil_Beneficiario` VARCHAR(500) NULL DEFAULT NULL,
  `perfil_Cliente` VARCHAR(500) NULL DEFAULT NULL,
  `soluciones_Alternativas` VARCHAR(500) NULL DEFAULT NULL,
  `importancia_Solucion` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`idDemanda`),
  INDEX `demanda_88d154de` (`idusuario` ASC),
  CONSTRAINT `idusuario_refs_id_7bb72c62`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`persona` (
  `user_ptr_id` INT(11) NOT NULL,
  `idpersona` INT(11) NOT NULL AUTO_INCREMENT,
  `identificacion` VARCHAR(20) NOT NULL,
  `cargo` VARCHAR(50) NOT NULL,
  `actividad` VARCHAR(150) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `areas_interes` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`idpersona`),
  UNIQUE INDEX `user_ptr_id` (`user_ptr_id` ASC),
  CONSTRAINT `user_ptr_id_refs_id_378c361a`
    FOREIGN KEY (`user_ptr_id`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`comentariodemanda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`comentariodemanda` (
  `idcomentario` INT(11) NOT NULL AUTO_INCREMENT,
  `idDemanda` INT(11) NOT NULL,
  `idpersona` INT(11) NOT NULL,
  `comentario` VARCHAR(500) NOT NULL,
  `calificacion` INT(11) NOT NULL,
  PRIMARY KEY (`idcomentario`),
  INDEX `comentarioDemanda_9da5d29d` (`idDemanda` ASC),
  INDEX `comentarioDemanda_88d154de` (`idpersona` ASC),
  CONSTRAINT `idDemanda_refs_idDemanda_9e481235`
    FOREIGN KEY (`idDemanda`)
    REFERENCES `redinnovacion`.`demanda` (`idDemanda`),
  CONSTRAINT `idpersona_refs_idpersona_4f07911b`
    FOREIGN KEY (`idpersona`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`oferta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`oferta` (
  `idOferta` INT(11) NOT NULL AUTO_INCREMENT,
  `idusuario` INT(11) NOT NULL,
  `tipoOferta` INT(11) NOT NULL,
  `estadoOferta` INT(11) NOT NULL,
  `calificacionGeneral` INT(11) NULL DEFAULT NULL,
  `ofertaPublicada` TINYINT(1) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  `dominio` VARCHAR(500) NOT NULL,
  `subdominio` VARCHAR(200) NOT NULL,
  `palabras_Claves` VARCHAR(200) NOT NULL,
  `tiempo_Inicio_Disponible` DATE NOT NULL,
  `tiempo_Fin_Disponible` DATE NOT NULL,
  `lugar_Aplicacion` VARCHAR(200) NOT NULL,
  `perfil_Beneficiario` VARCHAR(500) NULL DEFAULT NULL,
  `perfil_Cliente` VARCHAR(500) NULL DEFAULT NULL,
  `soluciones_Alternativas` VARCHAR(500) NULL DEFAULT NULL,
  `propuesta_Valor` VARCHAR(300) NULL DEFAULT NULL,
  `cuadro_Competidores` VARCHAR(100) NULL DEFAULT NULL,
  `cuadro_Tendencias_Relevantes` VARCHAR(100) NULL DEFAULT NULL,
  `estado_Propiedad_Intelectual` VARCHAR(500) NULL DEFAULT NULL,
  `evidencia_Traccion` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`idOferta`),
  INDEX `oferta_88d154de` (`idusuario` ASC),
  CONSTRAINT `idusuario_refs_id_19f5410d`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`comentariooferta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`comentariooferta` (
  `idcomentario` INT(11) NOT NULL AUTO_INCREMENT,
  `idOferta` INT(11) NOT NULL,
  `idpersona` INT(11) NOT NULL,
  `comentario` VARCHAR(500) NOT NULL,
  `calificacion` INT(11) NOT NULL,
  `pendienteRevision` TINYINT(1) NOT NULL,
  `aprobado` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idcomentario`),
  INDEX `comentarioOferta_73e67b22` (`idOferta` ASC),
  INDEX `comentarioOferta_88d154de` (`idpersona` ASC),
  CONSTRAINT `idOferta_refs_idOferta_7ac867bc`
    FOREIGN KEY (`idOferta`)
    REFERENCES `redinnovacion`.`oferta` (`idOferta`),
  CONSTRAINT `idpersona_refs_idpersona_7588e28f`
    FOREIGN KEY (`idpersona`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`concursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`concursos` (
  `idConcurso` INT(11) NOT NULL AUTO_INCREMENT,
  `idusuario` INT(11) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  `dominio` VARCHAR(200) NOT NULL,
  `subdominio` VARCHAR(200) NOT NULL,
  `fechaInicio` DATE NOT NULL,
  `fechaFin` DATE NOT NULL,
  `premios` VARCHAR(200) NOT NULL,
  `alcance` VARCHAR(300) NOT NULL,
  `num_finalistas` INT(11) NOT NULL,
  `perfil` VARCHAR(200) NOT NULL,
  `tipo_oferta` INT(11) NOT NULL,
  `estado` INT(11) NOT NULL,
  `imagen` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idConcurso`),
  INDEX `concursos_88d154de` (`idusuario` ASC),
  CONSTRAINT `idusuario_refs_id_dd12ca56`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`publicacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`publicacion` (
  `idpublicacion` INT(11) NOT NULL AUTO_INCREMENT,
  `idusuario` INT(11) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  `dominio` VARCHAR(200) NOT NULL,
  `subdominio` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idpublicacion`),
  INDEX `publicacion_88d154de` (`idusuario` ASC),
  CONSTRAINT `idusuario_refs_id_fcdc7503`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`convocatoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`convocatoria` (
  `idConvocatoria` INT(11) NOT NULL AUTO_INCREMENT,
  `fechaInicio` DATE NOT NULL,
  `fechaFin` DATE NOT NULL,
  `idpublicacionConvocatoria` INT(11) NOT NULL,
  PRIMARY KEY (`idConvocatoria`),
  INDEX `convocatoria_f6eeb65f` (`idpublicacionConvocatoria` ASC),
  CONSTRAINT `idpublicacionConvocatoria_refs_idpublicacion_bc2881b6`
    FOREIGN KEY (`idpublicacionConvocatoria`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`diagramacanvas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`diagramacanvas` (
  `iddiagramacanvas` INT(11) NOT NULL AUTO_INCREMENT,
  `idOferta` INT(11) NOT NULL,
  `asociacionesClave` VARCHAR(150) NULL DEFAULT NULL,
  `actividadesClave` VARCHAR(150) NULL DEFAULT NULL,
  `recursosClave` VARCHAR(150) NULL DEFAULT NULL,
  `propuestaValor` VARCHAR(150) NULL DEFAULT NULL,
  `relacionClientes` VARCHAR(150) NULL DEFAULT NULL,
  `segmentoMercado` VARCHAR(150) NULL DEFAULT NULL,
  `estructuraCostos` VARCHAR(150) NULL DEFAULT NULL,
  `fuenteIngresos` VARCHAR(150) NULL DEFAULT NULL,
  PRIMARY KEY (`iddiagramacanvas`),
  INDEX `diagramacanvas_73e67b22` (`idOferta` ASC),
  CONSTRAINT `idOferta_refs_idOferta_ebbd8cb9`
    FOREIGN KEY (`idOferta`)
    REFERENCES `redinnovacion`.`oferta` (`idOferta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`diagramaporter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`diagramaporter` (
  `iddiagramaPorter` INT(11) NOT NULL AUTO_INCREMENT,
  `idOferta` INT(11) NOT NULL,
  `rivalidadCompetidores` VARCHAR(200) NULL DEFAULT NULL,
  `competidoresPotenciales` VARCHAR(200) NULL DEFAULT NULL,
  `proveedores` VARCHAR(200) NULL DEFAULT NULL,
  `sustitutos` VARCHAR(200) NULL DEFAULT NULL,
  `consumidores` VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (`iddiagramaPorter`),
  INDEX `diagramaporter_73e67b22` (`idOferta` ASC),
  CONSTRAINT `idOferta_refs_idOferta_8a09ad88`
    FOREIGN KEY (`idOferta`)
    REFERENCES `redinnovacion`.`oferta` (`idOferta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_b7b81f0c` (`expire_date` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`django_site`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`django_site` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `domain` VARCHAR(100) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`equipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`equipo` (
  `idequipo` INT(11) NOT NULL AUTO_INCREMENT,
  `idOferta` INT(11) NOT NULL,
  `idpersona` INT(11) NOT NULL,
  `rol` VARCHAR(100) NOT NULL,
  `estado` INT(11) NOT NULL,
  PRIMARY KEY (`idequipo`),
  INDEX `equipo_54319a0f` (`idOferta` ASC),
  INDEX `equipo_88d154de` (`idpersona` ASC),
  CONSTRAINT `idOferta_refs_idOferta_e4728d4a`
    FOREIGN KEY (`idOferta`)
    REFERENCES `redinnovacion`.`oferta` (`idOferta`),
  CONSTRAINT `idpersona_refs_idpersona_5f95a377`
    FOREIGN KEY (`idpersona`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`imagendemanda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`imagendemanda` (
  `idimagen` INT(11) NOT NULL AUTO_INCREMENT,
  `idDemanda` INT(11) NOT NULL,
  `enlace_imagen` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idimagen`),
  INDEX `imagenDemanda_9da5d29d` (`idDemanda` ASC),
  CONSTRAINT `idDemanda_refs_idDemanda_71bc5e61`
    FOREIGN KEY (`idDemanda`)
    REFERENCES `redinnovacion`.`demanda` (`idDemanda`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`imagenoferta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`imagenoferta` (
  `idimagen` INT(11) NOT NULL AUTO_INCREMENT,
  `idOferta` INT(11) NOT NULL,
  `enlace_imagen` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idimagen`),
  INDEX `imagenOferta_73e67b22` (`idOferta` ASC),
  CONSTRAINT `idOferta_refs_idOferta_887f9dd9`
    FOREIGN KEY (`idOferta`)
    REFERENCES `redinnovacion`.`oferta` (`idOferta`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`incubacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`incubacion` (
  `idDetalleIncubacion` INT(11) NOT NULL AUTO_INCREMENT,
  `idusuario` INT(11) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  `dominio` VARCHAR(200) NOT NULL,
  `subdominio` VARCHAR(200) NOT NULL,
  `fechaInicio` DATE NOT NULL,
  `condiciones` VARCHAR(300) NOT NULL,
  `perfil_oferta` VARCHAR(200) NOT NULL,
  `tipo_oferta` INT(11) NOT NULL,
  `estado` INT(11) NOT NULL,
  `imagen` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idDetalleIncubacion`),
  INDEX `incubacion_88d154de` (`idusuario` ASC),
  CONSTRAINT `idusuario_refs_id_45b07ba9`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`institucion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`institucion` (
  `user_ptr_id` INT(11) NOT NULL,
  `idinstitucion` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre_corto` VARCHAR(20) NOT NULL,
  `descripcion` VARCHAR(900) NOT NULL,
  `mision` VARCHAR(900) NOT NULL,
  `sitio_web` VARCHAR(200) NOT NULL,
  `persona_que_registra` VARCHAR(200) NOT NULL,
  `idAdministrador` INT(11) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `recursos` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idinstitucion`),
  UNIQUE INDEX `user_ptr_id` (`user_ptr_id` ASC),
  CONSTRAINT `user_ptr_id_refs_id_fd310a34`
    FOREIGN KEY (`user_ptr_id`)
    REFERENCES `redinnovacion`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`institucion_persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`institucion_persona` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `idpersona` INT(11) NOT NULL,
  `idinstitucion` INT(11) NOT NULL,
  `cargoPersona` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `institucion_persona_8adb2a44` (`idpersona` ASC),
  INDEX `institucion_persona_a6094bcf` (`idinstitucion` ASC),
  CONSTRAINT `idinstitucion_refs_idinstitucion_b1def11b`
    FOREIGN KEY (`idinstitucion`)
    REFERENCES `redinnovacion`.`institucion` (`idinstitucion`),
  CONSTRAINT `idpersona_refs_idpersona_471c0464`
    FOREIGN KEY (`idpersona`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`mensaje`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`mensaje` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `idp_emisor` INT(11) NOT NULL,
  `idp_destino` INT(11) NOT NULL,
  `asunto` VARCHAR(50) NOT NULL,
  `txtMensaje` LONGTEXT NOT NULL,
  `fecha` DATE NOT NULL,
  `hora` TIME NOT NULL,
  `leido` TINYINT(1) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `mensaje_f28dad41` (`idp_emisor` ASC),
  INDEX `mensaje_12cc1b67` (`idp_destino` ASC),
  CONSTRAINT `idp_destino_refs_idpersona_8612e047`
    FOREIGN KEY (`idp_destino`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`),
  CONSTRAINT `idp_emisor_refs_idpersona_8612e047`
    FOREIGN KEY (`idp_emisor`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`milestone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`milestone` (
  `idMilestone` INT(11) NOT NULL AUTO_INCREMENT,
  `idpublicacion` INT(11) NOT NULL,
  `fecha_entrega` DATE NOT NULL,
  `requerimiento` VARCHAR(300) NOT NULL,
  `campo_nuevo` VARCHAR(300) NOT NULL,
  `peso` INT(11) NOT NULL,
  `calificacion` INT(11) NULL DEFAULT NULL,
  `estado` INT(11) NOT NULL,
  PRIMARY KEY (`idMilestone`),
  INDEX `milestone_5232bf5a` (`idpublicacion` ASC),
  CONSTRAINT `idpublicacion_refs_idpublicacion_68e2b755`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`solicitud`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`solicitud` (
  `idsolicitud` INT(11) NOT NULL AUTO_INCREMENT,
  `idpublicacion` INT(11) NOT NULL,
  `idofertapublicada` INT(11) NOT NULL,
  `fechaSol` DATE NOT NULL,
  PRIMARY KEY (`idsolicitud`),
  INDEX `solicitud_ed226d30` (`idpublicacion` ASC),
  INDEX `solicitud_69410e7c` (`idofertapublicada` ASC),
  CONSTRAINT `idofertapublicada_refs_idpublicacion_08615910`
    FOREIGN KEY (`idofertapublicada`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`),
  CONSTRAINT `idpublicacion_refs_idpublicacion_08615910`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`milestoneparticipante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`milestoneparticipante` (
  `idMilestoneparticipante` INT(11) NOT NULL AUTO_INCREMENT,
  `idmilestone` INT(11) NOT NULL,
  `idsolicitud` INT(11) NOT NULL,
  PRIMARY KEY (`idMilestoneparticipante`),
  INDEX `milestoneparticipante_5df947ef` (`idmilestone` ASC),
  INDEX `milestoneparticipante_46fc8fcc` (`idsolicitud` ASC),
  CONSTRAINT `idmilestone_refs_idMilestone_805c68fd`
    FOREIGN KEY (`idmilestone`)
    REFERENCES `redinnovacion`.`milestone` (`idMilestone`),
  CONSTRAINT `idsolicitud_refs_idsolicitud_abc008a4`
    FOREIGN KEY (`idsolicitud`)
    REFERENCES `redinnovacion`.`solicitud` (`idsolicitud`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`solicitudequipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`solicitudequipo` (
  `idSolicitudEquipo` INT(11) NOT NULL AUTO_INCREMENT,
  `idequipo` INT(11) NOT NULL,
  `idpersona` INT(11) NOT NULL,
  `pendienteRevision` TINYINT(1) NOT NULL,
  `aprobada` TINYINT(1) NOT NULL,
  PRIMARY KEY (`idSolicitudEquipo`),
  INDEX `solicitudEquipo_05b7cb86` (`idequipo` ASC),
  INDEX `solicitudEquipo_88d154de` (`idpersona` ASC),
  CONSTRAINT `idequipo_refs_idequipo_6e982415`
    FOREIGN KEY (`idequipo`)
    REFERENCES `redinnovacion`.`equipo` (`idequipo`),
  CONSTRAINT `idpersona_refs_idpersona_b50a17a3`
    FOREIGN KEY (`idpersona`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
