-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.23 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para base_datos
CREATE DATABASE IF NOT EXISTS `base_datos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `base_datos`;

-- Volcando estructura para tabla base_datos.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `CODIGO` char(10) NOT NULL DEFAULT '0',
  `NOMBRE` char(20) NOT NULL DEFAULT '0',
  `MODELO` char(20) NOT NULL DEFAULT '0',
  `PRECIO` char(50) NOT NULL DEFAULT '0',
  `CANTIDAD` char(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=188 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla base_datos.productos: ~19 rows (aproximadamente)
DELETE FROM `productos`;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`ID`, `CODIGO`, `NOMBRE`, `MODELO`, `PRECIO`, `CANTIDAD`) VALUES
	(39, 'RES001', 'RESISTENCIA', 'RV', '2.00', '222'),
	(40, 'TRAS-11', 'TRANSISTOR', 'PNP', '1.00', '554'),
	(44, '10101', 'CONDENSADOR', 'CERAMICO', '2.00', '100'),
	(168, 'DB121', 'DIODO', 'ZENER', '1.50', '231'),
	(169, 'IC002', 'IC', 'AND', '1.00', '200'),
	(170, 'IC003', 'IC', 'XOR', '1.00', '300'),
	(171, 'D0092', 'DIOD0', 'ZENER', '2.00', '232'),
	(172, 'RE21', 'RELE', '221R', '2.50', '423'),
	(173, '2560', 'ARDUINO', 'MEGA', '30.0', '37'),
	(174, '2021DS', 'ARDUINO', 'UNO R3', '15.50', '73'),
	(175, 'RES2021', 'RESISTENCIA', '4B', '0.10', '1000'),
	(176, 'LED122', 'LED', 'GREENR3', '0.50', '144'),
	(177, 'LDR43', 'LDR', 'LDRG', '2.00', '43'),
	(178, 'FUSI232', 'FUSIBLE', '23FDEW', '2.00', '331'),
	(179, 'MATRIZ32', 'MATRIZ', '32X8', '50.0', '56'),
	(180, 'SENSORRE', 'ULTRASONIC', 'RGR0544', '5.00', '231'),
	(181, '555N', 'TIMER', '555', '1.50', '621'),
	(182, 'ER43', 'PILAS', 'AAA', '2.00', '544'),
	(185, '1212', '12121', '12121', '22121', '12121');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
