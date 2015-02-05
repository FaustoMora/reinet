-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema redinnovacion
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema redinnovacion
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `redinnovacion` DEFAULT CHARACTER SET latin1 ;
USE `redinnovacion` ;

-- -----------------------------------------------------
-- Table `redinnovacion`.`catalogo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`catalogo` (
  `idcatalogo` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `codigo` VARCHAR(10) NULL DEFAULT NULL,
  `descripcion` VARCHAR(100) NULL DEFAULT NULL,
  `idcatalogopadre` BIGINT(20) NULL DEFAULT NULL,
  PRIMARY KEY (`idcatalogo`),
  INDEX `idcatalogopadre` (`idcatalogopadre` ASC),
  CONSTRAINT `catalogo_ibfk_1`
    FOREIGN KEY (`idcatalogopadre`)
    REFERENCES `redinnovacion`.`catalogo` (`idcatalogo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`usuario` (
  `idusuario` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL DEFAULT NULL,
  `password` VARCHAR(100) NULL DEFAULT NULL,
  `username` VARCHAR(100) NULL DEFAULT NULL,
  `foto_url` VARCHAR(200) NULL DEFAULT NULL,
  `ip_registro` VARCHAR(20) NULL DEFAULT NULL,
  PRIMARY KEY (`idusuario`),
  UNIQUE INDEX `idusuario` (`idusuario` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`publicacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`publicacion` (
  `idpublicacion` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idusuario` BIGINT(20) NOT NULL,
  `nombre` VARCHAR(150) NOT NULL,
  `descripcion` VARCHAR(500) NOT NULL,
  `dominio` INT(11) NOT NULL,
  `subdominio` INT(11) NOT NULL,
  PRIMARY KEY (`idpublicacion`),
  UNIQUE INDEX `idpublicacion_UNIQUE` (`idpublicacion` ASC),
  INDEX `idusuarioPublicacion_idx` (`idusuario` ASC),
  CONSTRAINT `idusuarioPublicacion`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`comentario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`comentario` (
  `idcomentario` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idusuario` BIGINT(20) NOT NULL,
  `comentario` VARCHAR(500) NOT NULL,
  `calificacion` INT(11) NULL DEFAULT NULL,
  `idpublicacion` BIGINT(20) NOT NULL,
  PRIMARY KEY (`idcomentario`),
  UNIQUE INDEX `idcomentario` (`idcomentario` ASC),
  INDEX `idpublicacionComentario_idx` (`idpublicacion` ASC),
  INDEX `idusuarioComentario_idx` (`idusuario` ASC),
  CONSTRAINT `idpublicacionComentario`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `idusuarioComentario`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`convocatoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`convocatoria` (
  `idConvocatoria` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `fechaInicio` DATE NOT NULL,
  `fechaFin` DATE NOT NULL,
  `idpublicacionConvocatoria` BIGINT(20) NOT NULL,
  PRIMARY KEY (`idConvocatoria`),
  UNIQUE INDEX `idConvocatoria` (`idConvocatoria` ASC),
  INDEX `idpublicacionConvocatoria` (`idpublicacionConvocatoria` ASC),
  CONSTRAINT `convocatoria_ibfk_1`
    FOREIGN KEY (`idpublicacionConvocatoria`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`detalleconcurso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`detalleconcurso` (
  `iddetalleconcurso` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `premios` VARCHAR(100) NOT NULL,
  `alcance` VARCHAR(100) NOT NULL,
  `num_finalistas` INT(11) NOT NULL,
  `perfil` VARCHAR(100) NOT NULL,
  `estado` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`iddetalleconcurso`),
  UNIQUE INDEX `iddetalleconcurso` (`iddetalleconcurso` ASC),
  INDEX `detalleconcurso_ibfk_1` (`idpublicacion` ASC),
  CONSTRAINT `detalleconcurso_ibfk_1`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`detalledemanda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`detalledemanda` (
  `iddetalledemanda` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `palabras_Claves` VARCHAR(100) NOT NULL,
  `tiempo_Inicio_Disponible` DATE NOT NULL,
  `tiempo_Fin_Disponible` DATE NOT NULL,
  `lugar_Aplicacion` VARCHAR(200) NOT NULL,
  `perfil_Beneficiario` VARCHAR(500) NOT NULL,
  `perfil_Cliente` VARCHAR(500) NOT NULL,
  `soluciones_Alternativas` VARCHAR(500) NOT NULL,
  `importancia_Solucion` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`iddetalledemanda`),
  UNIQUE INDEX `iddetalledemanda` (`iddetalledemanda` ASC),
  INDEX `idpublicacion_idx` (`idpublicacion` ASC),
  CONSTRAINT `idpublicaciondemanda`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`detalleincubacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`detalleincubacion` (
  `idDetalleIncubacion` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `fecha_inicio` DATE NOT NULL,
  `condiciones` VARCHAR(300) NOT NULL,
  `perfil_oferta` INT(11) NOT NULL,
  `tipo_oferta` INT(11) NOT NULL,
  PRIMARY KEY (`idDetalleIncubacion`),
  UNIQUE INDEX `idDetalleIncubacion` (`idDetalleIncubacion` ASC),
  INDEX `detalleincubacion_ibfk_1` (`idpublicacion` ASC),
  CONSTRAINT `detalleincubacion_ibfk_1`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`detalleoferta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`detalleoferta` (
  `iddetalleoferta` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NULL,
  `palabras_Claves` VARCHAR(100) NOT NULL,
  `tiempo_Inicio_Disponible` DATE NOT NULL,
  `tiempo_Fin_Disponible` DATE NOT NULL,
  `lugar_Aplicacion` VARCHAR(200) NOT NULL,
  `perfil_Beneficiario` VARCHAR(500) NOT NULL,
  `perfil_Cliente` VARCHAR(500) NOT NULL,
  `soluciones_Alternativas` VARCHAR(500) NULL DEFAULT NULL,
  `propuesta_Valor` VARCHAR(300) NULL DEFAULT NULL,
  `cuadro_Competidores` VARCHAR(100) NULL DEFAULT NULL,
  `cuadro_Tendencias_Relevantes` VARCHAR(100) NULL DEFAULT NULL,
  `estado_Propiedad_Intelectual` VARCHAR(500) NULL DEFAULT NULL,
  `evidencia_Traccion` VARCHAR(500) NULL DEFAULT NULL,
  PRIMARY KEY (`iddetalleoferta`),
  UNIQUE INDEX `iddetalleoferta` (`iddetalleoferta` ASC),
  INDEX `idpublicacion_idx` (`idpublicacion` ASC),
  CONSTRAINT `idpublicacionoferta`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `redinnovacion`.`diagramacanvas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`diagramacanvas` (
  `idDiagramaCanvas` BIGINT(20) NOT NULL,
  `iddetalleoferta` BIGINT(20) NOT NULL,
  `asociacionesClave` VARCHAR(150) NOT NULL,
  `actividadesClave` VARCHAR(150) NOT NULL,
  `recursosClave` VARCHAR(150) NOT NULL,
  `propuestaValor` VARCHAR(150) NOT NULL,
  `relacionClientes` VARCHAR(150) NOT NULL,
  `segmentoMercado` VARCHAR(150) NOT NULL,
  `estructuraCostos` VARCHAR(150) NOT NULL,
  `fuenteIngresos` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`idDiagramaCanvas`),
  INDEX `idOferta_idx` (`iddetalleoferta` ASC),
  CONSTRAINT `idOferta`
    FOREIGN KEY (`iddetalleoferta`)
    REFERENCES `redinnovacion`.`detalleoferta` (`iddetalleoferta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`diagramaporter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`diagramaporter` (
  `iddiagramaPorter` BIGINT(20) NOT NULL,
  `iddetalleoferta` BIGINT(20) NOT NULL,
  `rivalidadCompetidores` VARCHAR(200) NOT NULL,
  `competidoresPotenciales` VARCHAR(200) NOT NULL,
  `proveedores` VARCHAR(200) NOT NULL,
  `sustitutos` VARCHAR(200) NOT NULL,
  `consumidores` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`iddiagramaPorter`),
  INDEX `idOferta_idx` (`iddetalleoferta` ASC),
  CONSTRAINT `idOfertapub`
    FOREIGN KEY (`iddetalleoferta`)
    REFERENCES `redinnovacion`.`detalleoferta` (`iddetalleoferta`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`equipo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`equipo` (
  `idequipo` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `idusuario` BIGINT(20) NOT NULL,
  `rol` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idequipo`),
  INDEX `idpublicacion` (`idpublicacion` ASC),
  INDEX `idusuario` (`idusuario` ASC),
  CONSTRAINT `equipo_ibfk_1`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`),
  CONSTRAINT `equipo_ibfk_2`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`usuario` (`idusuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`imagen`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`imagen` (
  `idimagen` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `enlace_imagen` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`idimagen`),
  INDEX `idpubimagen_idx` (`idpublicacion` ASC),
  CONSTRAINT `idpubimagen`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`institucion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`institucion` (
  `idinstitucion` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `nombre_corto` VARCHAR(20) NOT NULL,
  `descripcion` VARCHAR(900) NOT NULL,
  `mision` VARCHAR(900) NOT NULL,
  `sitio_web` VARCHAR(200) NOT NULL,
  `persona_que_registra` VARCHAR(200) NOT NULL,
  `idAdministrador` BIGINT(20) UNSIGNED NOT NULL,
  `email` VARCHAR(50) NOT NULL,
  `telefono` VARCHAR(15) NOT NULL,
  `recursos` VARCHAR(100) NOT NULL,
  `idusuario` BIGINT(20) NOT NULL,
  PRIMARY KEY (`idinstitucion`),
  INDEX `idusuario` (`idusuario` ASC),
  CONSTRAINT `institucion_ibfk_1`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`usuario` (`idusuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`persona` (
  `idpersona` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `identificacion` VARCHAR(20) NOT NULL,
  `cargo` VARCHAR(50) NOT NULL,
  `actividad` VARCHAR(150) NOT NULL,
  `fecha_nacimiento` DATE NOT NULL,
  `areas_interes` VARCHAR(50) NOT NULL,
  `user_id` BIGINT(20),
  PRIMARY KEY (`idpersona`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`institucion_persona`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`institucion_persona` (
  `idpersona` BIGINT(20) NOT NULL,
  `idinstitucion` BIGINT(20) NOT NULL,
  INDEX `idpersona` (`idpersona` ASC),
  INDEX `idinstitucion` (`idinstitucion` ASC),
  CONSTRAINT `institucion_persona_ibfk_1`
    FOREIGN KEY (`idpersona`)
    REFERENCES `redinnovacion`.`persona` (`idpersona`),
  CONSTRAINT `institucion_persona_ibfk_2`
    FOREIGN KEY (`idinstitucion`)
    REFERENCES `redinnovacion`.`institucion` (`idinstitucion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`milestone`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`milestone` (
  `idmilestone` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `fecha_entrega` DATE NOT NULL,
  `requerimiento` VARCHAR(300) NOT NULL,
  `campo_nuevo` VARCHAR(300) NOT NULL,
  `peso` INT(11) NOT NULL,
  `calificacion` INT(11) NULL DEFAULT NULL,
  `estado` INT(11) NOT NULL,
  PRIMARY KEY (`idmilestone`),
  INDEX `idpublicacion` (`idpublicacion` ASC),
  CONSTRAINT `milestone_ibfk_1`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`solicitud`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`solicitud` (
  `idsolicitud` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idpublicacion` BIGINT(20) NOT NULL,
  `idofertapublicada` BIGINT(20) NOT NULL,
  `fecha` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idsolicitud`),
  INDEX `idpublicacion` (`idpublicacion` ASC),
  INDEX `idofertapublicada` (`idofertapublicada` ASC),
  CONSTRAINT `solicitud_ibfk_1`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`),
  CONSTRAINT `solicitud_ibfk_2`
    FOREIGN KEY (`idofertapublicada`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`milestoneparticipante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`milestoneparticipante` (
  `idmilestoneparticipante` BIGINT(20) NOT NULL AUTO_INCREMENT,
  `idmilestone` BIGINT(20) NOT NULL,
  `idsolicitud` BIGINT(20) NOT NULL,
  PRIMARY KEY (`idmilestoneparticipante`),
  INDEX `idmilestone` (`idmilestone` ASC),
  INDEX `idsolicitud` (`idsolicitud` ASC),
  CONSTRAINT `milestoneparticipante_ibfk_1`
    FOREIGN KEY (`idmilestone`)
    REFERENCES `redinnovacion`.`milestone` (`idmilestone`),
  CONSTRAINT `milestoneparticipante_ibfk_2`
    FOREIGN KEY (`idsolicitud`)
    REFERENCES `redinnovacion`.`solicitud` (`idsolicitud`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `redinnovacion`.`politicaprivacidad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `redinnovacion`.`politicaprivacidad` (
  `idusuario` BIGINT(20) NOT NULL,
  `idpublicacion` BIGINT(20) NOT NULL,
  `tipo_alcance` CHAR(50) NOT NULL,
  INDEX `idprivacidadpublicacion_idx` (`idpublicacion` ASC),
  INDEX `idprivacidadusuario` (`idusuario` ASC),
  CONSTRAINT `idprivacidadpublicacion`
    FOREIGN KEY (`idpublicacion`)
    REFERENCES `redinnovacion`.`publicacion` (`idpublicacion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idprivacidadusuario`
    FOREIGN KEY (`idusuario`)
    REFERENCES `redinnovacion`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
