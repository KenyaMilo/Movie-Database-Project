-- MySQL dump 10.13  Distrib 9.4.0, for macos15.4 (arm64)
--
-- Host: localhost    Database: MovieDatabase
-- ------------------------------------------------------
-- Server version	9.4.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Actor`
--

DROP TABLE IF EXISTS `Actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Actor` (
  `Actor_id` int NOT NULL,
  `First_name` varchar(45) DEFAULT NULL,
  `Last_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Actor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Actor`
--

LOCK TABLES `Actor` WRITE;
/*!40000 ALTER TABLE `Actor` DISABLE KEYS */;
INSERT INTO `Actor` VALUES (122856,'Jack','Black'),(135795,'Johnny','Depp'),(175966,'Chris','Hemsworth'),(246802,'Natalie','Portman'),(446902,'Scarlett','Johansson'),(629578,'Jennifer','Lawrence'),(754201,'Marilyn','Monroe'),(853301,'Morgan','Freeman'),(918273,'Harrison','Ford'),(987654,'Emma','Stone');
/*!40000 ALTER TABLE `Actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Acts_in`
--

DROP TABLE IF EXISTS `Acts_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Acts_in` (
  `Actor_Actor_id` int NOT NULL,
  `Movie_Movie_id` int NOT NULL,
  PRIMARY KEY (`Actor_Actor_id`,`Movie_Movie_id`),
  KEY `fk_Actor_has_Movie_Movie1_idx` (`Movie_Movie_id`),
  KEY `fk_Actor_has_Movie_Actor1_idx` (`Actor_Actor_id`),
  CONSTRAINT `fk_Actor_has_Movie_Actor1` FOREIGN KEY (`Actor_Actor_id`) REFERENCES `Actor` (`Actor_id`),
  CONSTRAINT `fk_Actor_has_Movie_Movie1` FOREIGN KEY (`Movie_Movie_id`) REFERENCES `Movie` (`Movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Acts_in`
--

LOCK TABLES `Acts_in` WRITE;
/*!40000 ALTER TABLE `Acts_in` DISABLE KEYS */;
INSERT INTO `Acts_in` VALUES (122856,121798),(135795,121798),(987654,121798),(246802,121978),(446902,121978),(918273,121978),(122856,294658),(135795,294658),(987654,294658),(135795,305542),(853301,305542),(987654,305542),(122856,478548),(135795,478548),(853301,585388),(918273,585388),(246802,614005),(446902,614005),(629578,614005),(122856,751896),(175966,751896),(629578,751896),(122856,831719),(175966,831719),(122856,896786),(754201,896786),(853301,896786);
/*!40000 ALTER TABLE `Acts_in` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Belongs_to`
--

DROP TABLE IF EXISTS `Belongs_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Belongs_to` (
  `Genre_Genre_id` int NOT NULL,
  `Movie_Movie_id` int NOT NULL,
  PRIMARY KEY (`Genre_Genre_id`,`Movie_Movie_id`),
  KEY `fk_Genre_has_Movie_Movie1_idx` (`Movie_Movie_id`),
  KEY `fk_Genre_has_Movie_Genre_idx` (`Genre_Genre_id`),
  CONSTRAINT `Genre_Genre_id` FOREIGN KEY (`Genre_Genre_id`) REFERENCES `Genre` (`Genre_id`),
  CONSTRAINT `Movie_Movie_id` FOREIGN KEY (`Movie_Movie_id`) REFERENCES `Movie` (`Movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Belongs_to`
--

LOCK TABLES `Belongs_to` WRITE;
/*!40000 ALTER TABLE `Belongs_to` DISABLE KEYS */;
INSERT INTO `Belongs_to` VALUES (956721,121798),(846342,121978),(670518,294658),(846342,294658),(846342,305542),(968025,305542),(846342,478548),(968025,478548),(456789,585388),(732871,614005),(846342,614005),(846342,751896),(765903,831719),(732871,896786);
/*!40000 ALTER TABLE `Belongs_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Directed_by`
--

DROP TABLE IF EXISTS `Directed_by`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Directed_by` (
  `Movie_Movie_id` int NOT NULL,
  `Director_Director_id` int NOT NULL,
  PRIMARY KEY (`Movie_Movie_id`,`Director_Director_id`),
  KEY `fk_Movie_has_Director_Director1_idx` (`Director_Director_id`),
  KEY `fk_Movie_has_Director_Movie1_idx` (`Movie_Movie_id`),
  CONSTRAINT `fk_Movie_has_Director_Director1` FOREIGN KEY (`Director_Director_id`) REFERENCES `Director` (`Director_id`),
  CONSTRAINT `fk_Movie_has_Director_Movie1` FOREIGN KEY (`Movie_Movie_id`) REFERENCES `Movie` (`Movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Directed_by`
--

LOCK TABLES `Directed_by` WRITE;
/*!40000 ALTER TABLE `Directed_by` DISABLE KEYS */;
INSERT INTO `Directed_by` VALUES (585388,113579),(121798,146802),(478548,146802),(751896,146802),(831719,234680),(585388,366802),(896786,586802),(121798,597913),(121978,597913),(121978,630246),(614005,723456),(305542,801234),(305542,990123);
/*!40000 ALTER TABLE `Directed_by` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Director`
--

DROP TABLE IF EXISTS `Director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Director` (
  `Director_id` int NOT NULL,
  `First_name` varchar(45) DEFAULT NULL,
  `Last_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Director`
--

LOCK TABLES `Director` WRITE;
/*!40000 ALTER TABLE `Director` DISABLE KEYS */;
INSERT INTO `Director` VALUES (113579,'Alfred','Hitchcock'),(146802,'Emilio','Fernandez'),(234680,'Nora','Ephron'),(366802,'Spike','Lee'),(586802,'John','Huston'),(597913,'Agnes','Varda'),(630246,'Sidney','Lumet'),(723456,'Chantal','Akerman'),(801234,'Stanley','Kubrick'),(990123,'Hayao','Miyazaki');
/*!40000 ALTER TABLE `Director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Genre`
--

DROP TABLE IF EXISTS `Genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genre` (
  `Genre_id` int NOT NULL,
  `Category` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Genre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genre`
--

LOCK TABLES `Genre` WRITE;
/*!40000 ALTER TABLE `Genre` DISABLE KEYS */;
INSERT INTO `Genre` VALUES (334497,'Science Fiction'),(456789,'Action'),(542261,'Western'),(670518,'Comedy'),(732871,'Fantasy'),(765903,'Thriller'),(845309,'Romance'),(846342,'Adventure'),(956721,'Horror'),(968025,'Musical');
/*!40000 ALTER TABLE `Genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Movie`
--

DROP TABLE IF EXISTS `Movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Movie` (
  `Movie_id` int NOT NULL,
  `Title` varchar(45) DEFAULT NULL,
  `Release_year` int DEFAULT NULL,
  PRIMARY KEY (`Movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Movie`
--

LOCK TABLES `Movie` WRITE;
/*!40000 ALTER TABLE `Movie` DISABLE KEYS */;
INSERT INTO `Movie` VALUES (121798,'Coraline',2009),(121978,'The Iron Giant',1999),(294658,'Toy Story',1995),(305542,'The Lion King',1994),(478548,'Coco',2017),(585388,'The Godfather',1972),(614005,'Spirited Away',2001),(751896,'Moana',2016),(831719,'Jaws',1975),(896786,'Up',2009);
/*!40000 ALTER TABLE `Movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Review` (
  `Review_id` int NOT NULL,
  `Rating` int DEFAULT NULL,
  `Movie_Movie_id` int DEFAULT NULL,
  PRIMARY KEY (`Review_id`),
  KEY `fk_Review_Movie1_idx` (`Movie_Movie_id`),
  CONSTRAINT `fk_Review_Movie1` FOREIGN KEY (`Movie_Movie_id`) REFERENCES `Movie` (`Movie_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Review`
--

LOCK TABLES `Review` WRITE;
/*!40000 ALTER TABLE `Review` DISABLE KEYS */;
INSERT INTO `Review` VALUES (123456,78,585388),(248420,81,831719),(270372,89,614005),(324700,50,121978),(398999,80,121978),(521197,96,478548),(649391,43,305542),(930639,75,294658),(969856,67,751896),(975311,91,896786);
/*!40000 ALTER TABLE `Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `User_id` varchar(25) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `Review_Review_id` int NOT NULL,
  PRIMARY KEY (`User_id`),
  KEY `fk_User_Review1_idx` (`Review_Review_id`),
  CONSTRAINT `fk_User_Review1` FOREIGN KEY (`Review_Review_id`) REFERENCES `Review` (`Review_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES ('alice','alice@email.com',969856),('angrybirds','angrybirds@email.com',270372),('beefeater','beefeater@emai.com',521197),('bigbadhat','bigbadhat@email.com',398999),('blueberyy','blueberry@email.com',649391),('chicken','chicken@email.com',324700),('froggy','froggy@email.com',123456),('scarypear','scarypear@email.com',930639),('tennisfan','tennisfan@email.com',975311),('yellowbear','yellowbear@email.com',248420);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-04 20:24:43
