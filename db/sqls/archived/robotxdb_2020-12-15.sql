# ************************************************************
# Sequel Pro SQL dump
# Version 5446
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 8.0.22)
# Database: robotxdb
# Generation Time: 2020-12-15 09:08:22 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table alembic_version
# ------------------------------------------------------------

DROP TABLE IF EXISTS `alembic_version`;

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;

INSERT INTO `alembic_version` (`version_num`)
VALUES
	('2ded8f41db80');

/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table anchorwaypoint
# ------------------------------------------------------------

DROP TABLE IF EXISTS `anchorwaypoint`;

CREATE TABLE `anchorwaypoint` (
  `aid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `globalx` decimal(11,9) DEFAULT NULL,
  `globaly` decimal(12,9) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table mission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `mission`;

CREATE TABLE `mission` (
  `mid` int DEFAULT NULL,
  `mname` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  `starttime` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table ranchors
# ------------------------------------------------------------

DROP TABLE IF EXISTS `ranchors`;

CREATE TABLE `ranchors` (
  `raid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `aid1` int DEFAULT NULL,
  `aid2` int DEFAULT NULL,
  `edge` float DEFAULT NULL,
  PRIMARY KEY (`raid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table rvehmis
# ------------------------------------------------------------

DROP TABLE IF EXISTS `rvehmis`;

CREATE TABLE `rvehmis` (
  `rvmid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `vid` int DEFAULT NULL,
  PRIMARY KEY (`rvmid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table rvehstateencounter
# ------------------------------------------------------------

DROP TABLE IF EXISTS `rvehstateencounter`;

CREATE TABLE `rvehstateencounter` (
  `rvseid` int NOT NULL AUTO_INCREMENT,
  `vsid` int DEFAULT NULL,
  `vsid2` int DEFAULT NULL,
  `commtype` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `range` float DEFAULT NULL,
  `rssi` float DEFAULT NULL,
  PRIMARY KEY (`rvseid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table vehicle
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicle`;

CREATE TABLE `vehicle` (
  `vid` int DEFAULT NULL,
  `vname` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table vehstate
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehstate`;

CREATE TABLE `vehstate` (
  `vsid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `vid` int DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `powerlevel` int DEFAULT NULL,
  `tempcpu` float DEFAULT NULL,
  `tempenv` float DEFAULT NULL,
  PRIMARY KEY (`vsid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table vehstatsanchor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehstatsanchor`;

CREATE TABLE `vehstatsanchor` (
  `vsaid` int NOT NULL AUTO_INCREMENT,
  `vsid` int DEFAULT NULL,
  `aid` int DEFAULT NULL,
  `commtype` varchar(8) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `range` float DEFAULT NULL,
  `rssi` float DEFAULT NULL,
  PRIMARY KEY (`vsaid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
