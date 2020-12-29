# ************************************************************
# Sequel Pro SQL dump
# Version 5446
#
# https://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 8.0.22)
# Database: robotxdb
# Generation Time: 2020-12-29 10:32:50 +0000
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
	('5b595d537279');

/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table anchor_waypoint
# ------------------------------------------------------------

DROP TABLE IF EXISTS `anchor_waypoint`;

CREATE TABLE `anchor_waypoint` (
  `aid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `globalx` decimal(11,9) DEFAULT NULL,
  `globaly` decimal(12,9) DEFAULT NULL,
  `uwbid` int DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table commtype
# ------------------------------------------------------------

DROP TABLE IF EXISTS `commtype`;

CREATE TABLE `commtype` (
  `cid` int NOT NULL AUTO_INCREMENT,
  `name` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table mission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `mission`;

CREATE TABLE `mission` (
  `mid` int NOT NULL AUTO_INCREMENT,
  `mname` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `starttime` datetime DEFAULT NULL,
  `endtime` datetime DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table r_anchors
# ------------------------------------------------------------

DROP TABLE IF EXISTS `r_anchors`;

CREATE TABLE `r_anchors` (
  `raid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `aid1` int DEFAULT NULL,
  `aid2` int DEFAULT NULL,
  `edge` float DEFAULT NULL,
  PRIMARY KEY (`raid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table r_uwb_veh
# ------------------------------------------------------------

DROP TABLE IF EXISTS `r_uwb_veh`;

CREATE TABLE `r_uwb_veh` (
  `mid` int NOT NULL AUTO_INCREMENT,
  `vid` int DEFAULT NULL,
  `uwbid` int DEFAULT NULL,
  `loc` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table r_veh_mis
# ------------------------------------------------------------

DROP TABLE IF EXISTS `r_veh_mis`;

CREATE TABLE `r_veh_mis` (
  `rvmid` int NOT NULL AUTO_INCREMENT,
  `mid` int DEFAULT NULL,
  `vid` int DEFAULT NULL,
  PRIMARY KEY (`rvmid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table r_vehstate_encounter
# ------------------------------------------------------------

DROP TABLE IF EXISTS `r_vehstate_encounter`;

CREATE TABLE `r_vehstate_encounter` (
  `rvseid` int NOT NULL AUTO_INCREMENT,
  `vsid` int DEFAULT NULL,
  `vsid2` int DEFAULT NULL,
  `commtypeid` int DEFAULT NULL,
  `range` float DEFAULT NULL,
  `rssi` float DEFAULT NULL,
  PRIMARY KEY (`rvseid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table uwb_module
# ------------------------------------------------------------

DROP TABLE IF EXISTS `uwb_module`;

CREATE TABLE `uwb_module` (
  `uwbid` int NOT NULL AUTO_INCREMENT,
  `address` blob,
  `serial` blob,
  PRIMARY KEY (`uwbid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;



# Dump of table vehicle
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehicle`;

CREATE TABLE `vehicle` (
  `vid` int NOT NULL AUTO_INCREMENT,
  `vname` varchar(32) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`vid`)
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



# Dump of table vehstats_anchor
# ------------------------------------------------------------

DROP TABLE IF EXISTS `vehstats_anchor`;

CREATE TABLE `vehstats_anchor` (
  `vsaid` int NOT NULL AUTO_INCREMENT,
  `vsid` int DEFAULT NULL,
  `aid` int DEFAULT NULL,
  `commtypeid` int DEFAULT NULL,
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
