/*
Navicat MySQL Data Transfer

Source Server         : intelligentCampus
Source Server Version : 50519
Source Host           : localhost:3306
Source Database       : intelligentcampustrain

Target Server Type    : MYSQL
Target Server Version : 50519
File Encoding         : 65001

Date: 2017-07-04 13:20:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for borrow
-- ----------------------------
DROP TABLE IF EXISTS `borrow`;
CREATE TABLE `borrow` (
  `student_id` int(10) NOT NULL,
  `book_id` text CHARACTER SET utf8mb4 NOT NULL,
  `brrow_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `book_name` text CHARACTER SET utf8mb4,
  KEY `student_id_index` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for card
-- ----------------------------
DROP TABLE IF EXISTS `card`;
CREATE TABLE `card` (
  `student_id` int(10) NOT NULL,
  `deal_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `deal_type` char(10) DEFAULT NULL,
  `deal_site` char(20) DEFAULT NULL,
  `deal_way` char(20) DEFAULT NULL,
  `deal_cost` float(10,2) DEFAULT NULL,
  `balance` float(10,0) DEFAULT NULL,
  KEY `student_id_index` (`student_id`) USING HASH
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for dorm
-- ----------------------------
DROP TABLE IF EXISTS `dorm`;
CREATE TABLE `dorm` (
  `student_id` int(10) NOT NULL,
  `date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `in_out` int(5) DEFAULT NULL,
  KEY `student_id_index` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for library
-- ----------------------------
DROP TABLE IF EXISTS `library`;
CREATE TABLE `library` (
  `student_id` int(10) NOT NULL,
  `date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `door_id` char(10) DEFAULT NULL,
  KEY `student_id_index` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for library_modify
-- ----------------------------
DROP TABLE IF EXISTS `library_modify`;
CREATE TABLE `library_modify` (
  `student_id` int(10) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `entrytime` time DEFAULT NULL,
  `leavetime` time DEFAULT NULL,
  `totaltime` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for score
-- ----------------------------
DROP TABLE IF EXISTS `score`;
CREATE TABLE `score` (
  `student_id` int(10) NOT NULL DEFAULT '0',
  `college_id` int(5) DEFAULT NULL,
  `rank` int(5) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `student_id` int(10) NOT NULL,
  `score` char(5) DEFAULT 'A' COMMENT '成绩排名',
  `cost_amount` char(5) DEFAULT 'A' COMMENT '花费金额',
  `cost_avg_superMarket` char(5) DEFAULT 'A',
  `cost_avg_laundryroom` char(5) DEFAULT NULL,
  `cost_avg_dinnerHall` char(5) DEFAULT 'A',
  `cost_rate_supermarket` char(5) DEFAULT 'A' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` char(5) DEFAULT 'A' COMMENT '花费在超市占总消费的比例',
  `cost_rate_dinnerhall` char(5) DEFAULT 'A' COMMENT '食堂消费占总消费的比例',
  `cost_times` char(5) DEFAULT 'A' COMMENT '花费次数',
  `library_borrow` char(5) DEFAULT 'A' COMMENT '图书借阅量',
  `library_times` char(5) DEFAULT 'A' COMMENT '勤奋度',
  `library_time_spand` char(5) DEFAULT 'A' COMMENT '图书馆时长',
  `balance_rank` char(5) DEFAULT 'A' COMMENT '卡内余额',
  `subsidy` char(5) DEFAULT 'A' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for subsidy
-- ----------------------------
DROP TABLE IF EXISTS `subsidy`;
CREATE TABLE `subsidy` (
  `student_id` int(10) NOT NULL DEFAULT '0',
  `stipend` int(10) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
