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
-- Table structure for table `room_master`
--

DROP TABLE IF EXISTS `room_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room_master` (
  `id` int NOT NULL AUTO_INCREMENT,
  `buildingid` int NOT NULL,
  `floorid` int NOT NULL,
  `roomname` varchar(255) NOT NULL,
  `roomtypename` varchar(75) NOT NULL,
  `createddatetime` datetime DEFAULT CURRENT_TIMESTAMP,
  `activestatus` int NOT NULL DEFAULT '1',
  `roomsubtypename` varchar(75) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room_master`
--

LOCK TABLES `room_master` WRITE;
/*!40000 ALTER TABLE `room_master` DISABLE KEYS */;
INSERT INTO `room_master` VALUES (1,1,1,'101','Teaching','2023-09-10 14:41:10',1,'Class Room'),(3,1,2,'103','Teaching','2023-09-10 15:20:14',1,'Class Room'),(5,3,5,'302','Non-Teaching','2023-09-13 17:25:00',1,'Bhajan Room'),(6,2,18,'XII-C','Teaching','2023-10-31 17:36:51',1,'Class Room'),(7,1,21,'104','Teaching','2023-11-02 15:28:39',1,'Lab'),(8,1,21,'105','Non-Teaching','2023-11-02 15:32:47',1,'Staff Room'),(9,1,1,'106','Non-Teaching','2023-11-02 15:33:28',1,'Store Room'),(10,3,22,'101','Teaching','2023-11-02 15:35:16',1,'Lab'),(11,3,22,'102','Non-Teaching','2023-11-02 15:35:33',1,'Sports Room'),(12,3,4,'201','Teaching','2023-11-02 15:35:46',1,'Class Room'),(13,3,4,'202','Non-Teaching','2023-11-02 15:35:59',1,'Staff Room'),(14,3,5,'301','Teaching','2023-11-02 15:36:10',1,'Class Room'),(15,3,5,'303','Non-Teaching','2023-11-02 15:36:31',1,'Waiting Hall'),(16,2,18,'XII-D','Teaching','2023-11-02 15:40:53',1,'Class Room'),(17,2,18,'XII-A','Teaching','2023-11-02 15:41:13',1,'Class Room'),(18,2,18,'XII-B','Teaching','2023-11-02 17:27:59',1,'Class Room'),(19,2,18,'XII-E','Teaching','2023-11-02 17:28:42',1,'Class Room'),(20,2,18,'XII-F','Teaching','2023-11-02 17:29:01',1,'Class Room'),(21,2,18,'XII-G','Teaching','2023-11-02 17:29:28',1,'Class Room'),(22,2,18,'Staff Room','Non-Teaching','2023-11-02 17:31:36',1,'Staff Room'),(23,2,18,'Store Room','Non-Teaching','2023-11-02 17:32:01',1,'Store Room'),(27,2,19,'XI-A','Teaching','2023-11-02 17:34:48',1,'Class Room'),(28,2,19,'XI-B','Teaching','2023-11-02 17:35:17',1,'Class Room'),(29,2,19,'XI-C','Teaching','2023-11-02 17:35:34',1,'Class Room'),(30,2,19,'XI-D','Teaching','2023-11-02 17:35:52',1,'Class Room'),(31,2,19,'XI-E','Teaching','2023-11-02 17:36:21',1,'Class Room'),(32,2,19,'XI-F','Teaching','2023-11-02 17:36:41',1,'Class Room'),(33,2,19,'Staff Room','Non-Teaching','2023-11-02 17:37:03',1,'Staff Room'),(35,2,19,'Store Room','Non-Teaching','2023-11-02 17:37:56',1,'Store Room'),(36,2,19,'IX and X  C.S Lab','Teaching','2023-11-02 17:39:25',1,'Lab'),(37,2,19,'XI and XII  C.S Lab','Teaching','2023-11-02 17:39:46',1,'Lab'),(38,2,20,'X-A','Teaching','2023-11-02 17:40:35',1,'Class Room'),(39,2,20,'X-B','Teaching','2023-11-02 17:40:51',1,'Class Room'),(40,2,20,'X-C','Teaching','2023-11-02 17:41:06',1,'Class Room'),(41,2,20,'X-D','Teaching','2023-11-02 17:41:56',1,'Class Room'),(42,2,20,'X-E','Teaching','2023-11-02 17:42:07',1,'Class Room'),(43,2,20,'X-F','Teaching','2023-11-02 17:42:20',1,'Class Room'),(44,2,20,'X-G','Teaching','2023-11-02 17:42:33',1,'Class Room'),(45,2,20,'X-H','Teaching','2023-11-02 17:42:45',1,'Class Room'),(46,2,20,'X-I','Teaching','2023-11-02 17:43:04',1,'Class Room'),(47,2,20,'X-J','Teaching','2023-11-02 17:43:20',1,'Class Room'),(48,2,20,'X-K','Teaching','2023-11-02 17:43:31',1,'Class Room'),(49,2,20,'Staff Room','Non-Teaching','2023-11-02 17:43:49',1,'Staff Room'),(50,2,20,'VP Room','Non-Teaching','2023-11-02 17:44:14',1,'Staff Room');
/*!40000 ALTER TABLE `room_master` ENABLE KEYS */;
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
