-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 22, 2023 at 07:42 AM
-- Server version: 8.0.27
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `category_name` text,
  `status` text,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`category_id`, `category_name`, `status`) VALUES
(11, 'Regina Peterson', 'False'),
(10, 'Hasad Sharpe', 'False'),
(9, 'Luke Estrada', 'True'),
(8, 'Chase Sing', 'False'),
(12, 'Yvonne Harris', 'False'),
(25, 'Clothe', 'True'),
(23, 'Beberage', 'True'),
(24, 'Drink', 'False');

-- --------------------------------------------------------

--
-- Table structure for table `currency`
--

DROP TABLE IF EXISTS `currency`;
CREATE TABLE IF NOT EXISTS `currency` (
  `id` int NOT NULL AUTO_INCREMENT,
  `code` text,
  `symbol` text,
  `is_default` varchar(25) DEFAULT NULL,
  `sell_out_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `currency`
--

INSERT INTO `currency` (`id`, `code`, `symbol`, `is_default`, `sell_out_price`) VALUES
(5, 'Deserunt enim omnis ', 'Aut quae distinctio', 'False', '692.00'),
(6, 'Sit laborum Molesti', 'Et fugit quia sit ', 'False', '624.00'),
(7, 'Aut iure laudantium', 'Adipisci perspiciati', 'False', '744.00'),
(8, 'Labore quis doloribu', 'Numquam consequatur', 'False', '319.00');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `image` text,
  `status` text,
  `phone` text,
  `email` text,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`customer_id`, `name`, `image`, `status`, `phone`, `email`) VALUES
(10, NULL, NULL, NULL, NULL, NULL),
(5, 'Lilah Wall', NULL, 'True', '012342234', 'lila@gmail.com'),
(6, 'Amaya Cline', NULL, 'True', NULL, NULL),
(8, 'Neve Burke', NULL, 'True', NULL, NULL),
(9, 'Shannon Valenzuela', NULL, 'True', NULL, NULL),
(11, 'duck', NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `order_detail`
--

DROP TABLE IF EXISTS `order_detail`;
CREATE TABLE IF NOT EXISTS `order_detail` (
  `order_detail_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`order_detail_id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `order_table`
--

DROP TABLE IF EXISTS `order_table`;
CREATE TABLE IF NOT EXISTS `order_table` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `order_date` date DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
CREATE TABLE IF NOT EXISTS `payment` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `order_id` (`order_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` text,
  `price` decimal(10,2) DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `image` text,
  `status` text,
  `category_id` int DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  KEY `category_id` (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `price`, `discount`, `image`, `status`, `category_id`) VALUES
(34, 'Acc Church', '43.00', '100.00', NULL, 'False', 8),
(33, 'Kimberly Gentry', '198.00', '94.00', NULL, 'True', 10),
(32, 'Vaughan Mosley', '227.00', '37.00', NULL, 'True', 12),
(31, 'Ezra Albert', '891.00', '90.00', NULL, 'True', 11),
(30, 'Tara Klein', '212.00', '58.00', NULL, 'True', 8),
(29, 'Jason Massey', '851.00', '22.00', NULL, 'True', 9),
(28, 'Sarah Hutchinson', '177.00', '83.00', NULL, 'True', 9),
(27, 'Cailin Reeves', '420.00', '29.00', NULL, 'True', 8),
(26, 'Ivory Walters', '148.00', '14.00', NULL, 'False', 11),
(25, 'Raya Patton', '953.00', '69.00', NULL, 'True', 11),
(24, 'Thor Tyson', '184.00', '92.00', NULL, 'True', 10),
(35, 'Ross Juarez', '68.00', '18.00', NULL, 'True', 9);

-- --------------------------------------------------------

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
CREATE TABLE IF NOT EXISTS `sale` (
  `sale_id` int NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `price` decimal(10,2) NOT NULL,
  `customer_id` int NOT NULL,
  PRIMARY KEY (`sale_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `sale`
--

INSERT INTO `sale` (`sale_id`, `date`, `price`, `customer_id`) VALUES
(1, '2023-12-16 00:00:00', '0.00', 1),
(2, '2023-12-16 00:00:00', '0.00', 1),
(3, '2023-12-16 00:00:00', '0.00', 1),
(4, '2023-12-21 17:42:50', '0.00', 1),
(5, '2023-12-21 17:43:41', '0.00', 1),
(6, '2023-12-21 18:09:40', '99.00', 1),
(7, '2023-12-21 18:10:26', '1039.00', 1),
(8, '2023-12-21 19:54:46', '1118.00', 1),
(9, '2023-12-21 21:21:14', '1118.00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `image` text,
  `status` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `name`, `image`, `status`) VALUES
(3, 'Regan Snyder', NULL, 'True'),
(4, 'Cheryl Yates', NULL, 'False'),
(5, 'Alana Mejia', NULL, 'False'),
(6, 'Aquila Gentry', NULL, 'False'),
(7, 'Jacob Delaney', NULL, 'False');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
