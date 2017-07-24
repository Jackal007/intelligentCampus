/*
Navicat MySQL Data Transfer

Source Server         : gdafgadfg
Source Server Version : 50519
Source Host           : localhost:3306
Source Database       : intelligentcampustrain

Target Server Type    : MYSQL
Target Server Version : 50519
File Encoding         : 65001

Date: 2017-07-07 18:33:08
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
-- Table structure for card_2
-- ----------------------------
DROP TABLE IF EXISTS `card_2`;
CREATE TABLE `card_2` (
  `studentid` int(10) NOT NULL,
  `date` date NOT NULL,
  `date_cost` float(10,2) DEFAULT NULL,
  PRIMARY KEY (`studentid`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for college_info
-- ----------------------------
DROP TABLE IF EXISTS `college_info`;
CREATE TABLE `college_info` (
  `college_id` int(11) NOT NULL,
  `2000_num` int(11) DEFAULT NULL,
  `1500_num` int(11) DEFAULT NULL,
  `1000_num` int(11) DEFAULT NULL,
  `stu_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
  `score` float(10,0) DEFAULT '0' COMMENT '成绩排名',
  `cost_amount` float(10,0) DEFAULT '0' COMMENT '花费金额',
  `cost_variance` float(10,0) DEFAULT '0',
  `cost_avg_day_superMarket` float(10,0) DEFAULT '0',
  `cost_avg_day_laundryroom` float(10,0) DEFAULT '0',
  `cost_avg_day_dinnerHall` float(10,0) DEFAULT '0',
  `cost_rate_supermarket` float(10,0) DEFAULT '0' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` float(10,0) DEFAULT '0' COMMENT '花费在超市占总消费的比例',
  `cost_rate_dinnerhall` float(10,0) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` float(10,0) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_dinnerhall` float(10,0) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_laundry` float(10,0) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times` float(10,0) DEFAULT '0' COMMENT '花费次数',
  `library_borrow` float(10,0) DEFAULT '0' COMMENT '图书借阅量',
  `library_times` float(10,0) DEFAULT '0' COMMENT '勤奋度',
  `library_time_spand` float(10,0) DEFAULT '0' COMMENT '图书馆时长',
  `balance_rank` float(10,0) DEFAULT '0' COMMENT '卡内余额',
  `card_days` float(10,0) DEFAULT '0' COMMENT 'card活跃天数',
  `time6_7costs` float(10,0) DEFAULT '0' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` float(10,0) DEFAULT '0' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` float(10,0) DEFAULT '0' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` float(10,0) DEFAULT '0' COMMENT '该学生的日平均消费',
  `consumetimes11_12` float(10,0) DEFAULT '0' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` float(10,0) DEFAULT '0' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` float(10,0) DEFAULT '0' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` float(10,0) DEFAULT '0' COMMENT '卡充值总额',
  `maxcost7_8` float(10,0) DEFAULT '0' COMMENT '7点 -8点间的最大单笔消费',
  `subsidy` float(10,0) DEFAULT '0' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for students_old
-- ----------------------------
DROP TABLE IF EXISTS `students_old`;
CREATE TABLE `students_old` (
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
-- Table structure for students_rank
-- ----------------------------
DROP TABLE IF EXISTS `students_rank`;
CREATE TABLE `students_rank` (
  `student_id` int(10) NOT NULL,
  `score` int(3) DEFAULT '0' COMMENT '成绩排名',
  `cost_amount` int(3) DEFAULT '0' COMMENT '花费金额',
  `cost_variance` int(3) DEFAULT '0',
  `cost_avg_day_superMarket` int(3) DEFAULT '0',
  `cost_avg_day_laundryroom` int(3) DEFAULT '0',
  `cost_avg_day_dinnerHall` int(3) DEFAULT '0',
  `cost_rate_supermarket` int(3) DEFAULT '0' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` int(3) DEFAULT '0' COMMENT '花费在超市占总消费的比例',
  `cost_rate_dinnerhall` int(3) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` int(3) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_dinnerhall` int(3) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_laundry` int(3) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times` int(3) DEFAULT '0' COMMENT '花费次数',
  `library_borrow` int(3) DEFAULT '0' COMMENT '图书借阅量',
  `library_times` int(3) DEFAULT '0' COMMENT '勤奋度',
  `library_time_spand` int(3) DEFAULT '0' COMMENT '图书馆时长',
  `balance_rank` int(3) DEFAULT '0' COMMENT '卡内余额',
  `card_days` int(3) DEFAULT '0' COMMENT 'card活跃天数',
  `time6_7costs` int(3) DEFAULT '0' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` int(3) DEFAULT '0' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` int(3) DEFAULT '0' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` int(3) DEFAULT '0' COMMENT '该学生的日平均消费',
  `consumetimes11_12` int(3) DEFAULT '0' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` int(3) DEFAULT '0' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` int(3) DEFAULT '0' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` int(3) DEFAULT '0' COMMENT '卡充值总额',
  `maxcost7_8` int(3) DEFAULT '0' COMMENT '7点 -8点间的最大单笔消费',
  `subsidy` int(3) DEFAULT '0' COMMENT '奖学金额',
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
