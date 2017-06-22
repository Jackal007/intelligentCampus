/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50624
Source Host           : localhost:3306
Source Database       : intelligentcampus

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2017-06-22 10:36:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `students`
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `student_id` varchar(50) NOT NULL,
  `score` float(5,0) DEFAULT '-1' COMMENT '成绩排名',
  `cost_amount` float(5,0) DEFAULT '-1' COMMENT '花费金额',
  `cost_avg_superMarket` float(5,0) DEFAULT NULL,
  `cost_avg_dinnerHall` float(5,0) DEFAULT NULL,
  `cost_supermarket_rate` float(5,0) DEFAULT '-1' COMMENT '花费在超市占总消费的比例',
  `cost_dinnerhall_rate` float(5,0) DEFAULT '-1' COMMENT '食堂消费占总消费的比例',
  `cost_times` float(5,0) DEFAULT '-1' COMMENT '花费次数',
  `library_borrow` float(5,0) DEFAULT '-1' COMMENT '图书借阅量',
  `library_times` float(5,0) DEFAULT '-1' COMMENT '勤奋度',
  `library_time_spand` float(5,0) DEFAULT '-1' COMMENT '图书馆时长',
  `balance_rank` float(5,0) DEFAULT '-1' COMMENT '卡内余额',
  `subsidy` float(5,0) DEFAULT '-1' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of students
-- ----------------------------
