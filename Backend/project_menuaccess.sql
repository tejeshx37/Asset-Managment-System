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
-- Table structure for table `menuaccess`
--

DROP TABLE IF EXISTS `menuaccess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `menuaccess` (
  `id` int NOT NULL AUTO_INCREMENT,
  `menuid` int DEFAULT NULL,
  `profileid` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `menuid` (`menuid`),
  KEY `profileid` (`profileid`),
  CONSTRAINT `menuaccess_ibfk_1` FOREIGN KEY (`menuid`) REFERENCES `menudetails` (`menuid`),
  CONSTRAINT `menuaccess_ibfk_2` FOREIGN KEY (`profileid`) REFERENCES `profile` (`profileid`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menuaccess`
--

LOCK TABLES `menuaccess` WRITE;
/*!40000 ALTER TABLE `menuaccess` DISABLE KEYS */;
INSERT INTO `menuaccess` VALUES (17,1,3),(18,2,3),(19,3,3),(20,4,3),(21,8,3),(22,5,4),(23,6,4),(24,8,4),(93,1,2),(94,2,2),(95,3,2),(96,4,2),(97,5,2),(98,6,2),(99,7,2),(100,8,2),(101,9,2),(102,10,2),(103,21,2),(104,23,2),(105,24,2),(106,1,1),(107,2,1),(108,3,1),(109,4,1),(110,5,1),(111,6,1),(112,7,1),(113,8,1),(114,9,1),(115,10,1),(116,21,1),(117,23,1),(118,24,1);
/*!40000 ALTER TABLE `menuaccess` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-05 22:38:04
