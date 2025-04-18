-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: project
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile` (
  `profileid` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(90) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `phoneno` bigint DEFAULT NULL,
  `paswd` varchar(50) NOT NULL,
  `actstatus` int NOT NULL DEFAULT '1',
  `datime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `motime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `userid` varchar(25) DEFAULT NULL,
  `resetpwd` int DEFAULT '1',
  PRIMARY KEY (`profileid`),
  UNIQUE KEY `userid` (`userid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1,'Tejesh','12 MGR Nagar velachery chennai-42','tejeshsms@gmail',90425128,'Tejesh#12345678',1,'2023-05-30 00:00:00','2023-05-30 00:00:00','0901005',0),(2,'admin','22 MGR NAGAR VELACHERRY','admin@gmail.com',6548534978,'Tejesh#1234567',1,'2023-07-23 00:00:00','2023-07-23 00:00:00','admin',0),(3,'Solai priydharshan','22 MGR NAGAR adambakkam','solai@gmail.com',8648534901,'Solai#123',1,'2023-07-23 00:00:00','2023-07-23 00:00:00','SN1',0),(4,'Rajat','12 MGR NAGAR velachery','Rajat@gmail.com',9868953478,'Rajat#1234',1,'2023-07-23 00:00:00','2023-07-23 00:00:00','RT1',0),(10,'Vice president','13th Balaji nagar adambakkam','DavVp_2010@gmail.com',9407324222,'VP6375',1,'2023-11-04 18:41:42','2023-11-04 18:41:42','5',1),(11,'Teacher','14th balaji nagar adambakkam','davteach_7238@gmail.com',9144602608,'Teach36963',1,'2023-11-04 18:43:28','2023-11-04 18:43:28','6',1);
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-05 22:38:03
