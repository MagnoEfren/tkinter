
CREATE DATABASE IF NOT EXISTS `base_datos` ;
USE `base_datos`;

-- Volcando estructura para tabla base_datos.login_datos
CREATE TABLE IF NOT EXISTS `login_datos` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Users` varchar(50) NOT NULL DEFAULT '0',
  `Password` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

