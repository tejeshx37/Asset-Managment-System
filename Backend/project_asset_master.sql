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
-- Table structure for table `asset_master`
--

DROP TABLE IF EXISTS `asset_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asset_master` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(75) NOT NULL,
  `desc1` varchar(255) NOT NULL,
  `createddatetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `activestatus` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_master`
--

LOCK TABLES `asset_master` WRITE;
/*!40000 ALTER TABLE `asset_master` DISABLE KEYS */;
INSERT INTO `asset_master` VALUES (1,'Tube Light','both tube and led','2023-09-10 16:20:17',1),(2,'Blub','','2023-09-10 16:20:33',1),(3,'Fan','','2023-09-10 16:20:38',1),(4,'Camera','','2023-09-10 16:20:43',1),(5,'Book Rack','','2023-09-10 16:20:55',1),(6,'Table','','2023-09-10 16:21:42',1),(7,'Chair','','2023-09-10 16:21:50',1),(8,'TV','Both LED  and LCD','2023-09-10 16:22:23',1),(9,'Projector','','2023-09-10 16:22:37',1),(10,'Sense Board','Smart Board','2023-11-02 17:49:47',1),(11,'Bench','','2023-11-02 17:53:12',1);
/*!40000 ALTER TABLE `asset_master` ENABLE KEYS */;
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
