/*
Navicat MySQL Data Transfer

Source Server         : gdafgadfg
Source Server Version : 50519
Source Host           : localhost:3306
Source Database       : intelligentcampustrain

Target Server Type    : MYSQL
Target Server Version : 50519
File Encoding         : 65001

Date: 2017-07-24 13:37:19
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
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

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
-- Table structure for id
-- ----------------------------
DROP TABLE IF EXISTS `id`;
CREATE TABLE `id` (
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
  `score` float(15,5) DEFAULT '0.00000' COMMENT '成绩排名',
  `cost_amount` float(15,5) DEFAULT '0.00000' COMMENT '花费金额',
  `cost_variance` float(15,5) DEFAULT '0.00000' COMMENT '消费方差',
  `cost_avg_day_superMarket` float(15,5) DEFAULT '0.00000' COMMENT '每天超市消费平均值',
  `cost_avg_day_laundryroom` float(15,5) DEFAULT '0.00000' COMMENT '每天洗衣房消费平均值',
  `cost_avg_day_dinnerHall` float(15,5) DEFAULT '0.00000' COMMENT '每天食堂消费平均值',
  `cost_rate_supermarket` float(15,5) DEFAULT '0.00000' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` float(15,5) DEFAULT '0.00000' COMMENT '花费在洗衣房占总消费的比例',
  `cost_rate_dinnerhall` float(15,5) DEFAULT '0.00000' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` float(15,5) DEFAULT '0.00000' COMMENT '每天超市消费平均值',
  `cost_times_day_dinnerhall` float(15,5) DEFAULT '0.00000' COMMENT '每天食堂消费平均值',
  `cost_times_day_laundryroom` float(15,5) DEFAULT '0.00000' COMMENT '每天洗衣房消费平均值',
  `cost_times` float(15,5) DEFAULT '0.00000' COMMENT '花费次数',
  `library_borrow` float(15,5) DEFAULT '0.00000' COMMENT '图书借阅量',
  `library_times` float(15,5) DEFAULT '0.00000' COMMENT '进图书馆次数',
  `library_time_spand` float(15,5) DEFAULT '0.00000' COMMENT '图书馆时长',
  `balance_rank` float(15,5) DEFAULT '0.00000' COMMENT '卡内余额',
  `card_days` float(15,5) DEFAULT '0.00000' COMMENT 'card活跃天数',
  `time6_7costs` float(15,5) DEFAULT '0.00000' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` float(15,5) DEFAULT '0.00000' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` float(15,5) DEFAULT '0.00000' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` float(15,5) DEFAULT '0.00000' COMMENT '该学生的日平均消费',
  `consumetimes11_12` float(15,5) DEFAULT '0.00000' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` float(15,5) DEFAULT '0.00000' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` float(15,5) DEFAULT '0.00000' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` float(15,5) DEFAULT '0.00000' COMMENT '卡充值总额',
  `maxcost7_8` float(15,5) DEFAULT '0.00000' COMMENT '7点 -8点间的最大单笔消费',
  `below10_rank` float(15,5) DEFAULT '0.00000' COMMENT '日消费金额小于10天数占比',
  `below2_5_rank` float(15,5) DEFAULT '0.00000' COMMENT '单次消费金额小于2.5次数占比',
  `propotion_of_2000` float(15,5) DEFAULT '0.00000' COMMENT '所在学院获得2000助学金占所有获得学生比例',
  `propotion_of_1500` float(15,5) DEFAULT '0.00000' COMMENT '所在学院获得1500助学金占所有获得学生比例',
  `scorerank_divided_by_stunum` float(15,5) DEFAULT '0.00000' COMMENT '成绩排名除以学院学生人数',
  `propotion_of_1000` float(15,5) DEFAULT '0.00000' COMMENT '所在学院获得1000助学金占所有获得学生比例',
  `score_rank*consume_rank` float(15,5) DEFAULT '0.00000' COMMENT '成绩排名乘以消费排名',
  `consume_rank` float(15,5) DEFAULT '0.00000' COMMENT '消费排名',
  `time7_8consume_avg` float(15,5) DEFAULT '0.00000' COMMENT '7点 -8点间的平均消费',
  `avg_charge` float(15,5) DEFAULT '0.00000' COMMENT '平均充值金额',
  `subsidy` float(15,5) DEFAULT '0.00000' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for students_rank
-- ----------------------------
DROP TABLE IF EXISTS `students_rank`;
CREATE TABLE `students_rank` (
  `student_id` int(10) NOT NULL,
  `score` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名',
  `cost_amount` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费金额',
  `cost_variance` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费方差',
  `cost_avg_day_superMarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_avg_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_avg_day_dinnerHall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_rate_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在洗衣房占总消费的比例',
  `cost_rate_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_times_day_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_times_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费次数',
  `library_borrow` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书借阅量',
  `library_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '进图书馆次数',
  `library_time_spand` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书馆时长',
  `balance_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡内余额',
  `card_days` int(3) unsigned zerofill DEFAULT '000' COMMENT 'card活跃天数',
  `time6_7costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生的日平均消费',
  `consumetimes11_12` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡充值总额',
  `maxcost7_8` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的最大单笔消费',
  `below10_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '日消费金额小于10天数占比',
  `below2_5_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '单次消费金额小于2.5次数占比',
  `propotion_of_2000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得2000助学金占所有获得学生比例',
  `propotion_of_1500` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1500助学金占所有获得学生比例',
  `scorerank_divided_by_stunum` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名除以学院学生人数',
  `propotion_of_1000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1000助学金占所有获得学生比例',
  `score_rank*consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名乘以消费排名',
  `consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费排名',
  `time7_8consume_avg` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的平均消费',
  `avg_charge` int(3) unsigned zerofill DEFAULT '000' COMMENT '平均充值金额',
  `subsidy` int(3) unsigned zerofill DEFAULT '000' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for students_rank_copy
-- ----------------------------
DROP TABLE IF EXISTS `students_rank_copy`;
CREATE TABLE `students_rank_copy` (
  `student_id` int(10) NOT NULL,
  `score` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名',
  `cost_amount` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费金额',
  `cost_variance` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费方差',
  `cost_avg_day_superMarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_avg_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_avg_day_dinnerHall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_rate_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在洗衣房占总消费的比例',
  `cost_rate_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_times_day_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_times_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费次数',
  `library_borrow` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书借阅量',
  `library_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '进图书馆次数',
  `library_time_spand` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书馆时长',
  `balance_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡内余额',
  `card_days` int(3) unsigned zerofill DEFAULT '000' COMMENT 'card活跃天数',
  `time6_7costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生的日平均消费',
  `consumetimes11_12` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡充值总额',
  `maxcost7_8` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的最大单笔消费',
  `below10_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '日消费金额小于10天数占比',
  `below2_5_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '单次消费金额小于2.5次数占比',
  `propotion_of_2000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得2000助学金占所有获得学生比例',
  `propotion_of_1500` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1500助学金占所有获得学生比例',
  `scorerank_divided_by_stunum` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名除以学院学生人数',
  `propotion_of_1000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1000助学金占所有获得学生比例',
  `score_rank*consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名乘以消费排名',
  `consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费排名',
  `time7_8consume_avg` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的平均消费',
  `avg_charge` int(3) unsigned zerofill DEFAULT '000' COMMENT '平均充值金额',
  `subsidy` int(3) unsigned zerofill DEFAULT '000' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for students_rank_copy2
-- ----------------------------
DROP TABLE IF EXISTS `students_rank_copy2`;
CREATE TABLE `students_rank_copy2` (
  `student_id` int(10) NOT NULL,
  `score` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名',
  `cost_amount` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费金额',
  `cost_variance` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费方差',
  `cost_avg_day_superMarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_avg_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_avg_day_dinnerHall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_rate_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在洗衣房占总消费的比例',
  `cost_rate_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_times_day_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_times_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费次数',
  `library_borrow` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书借阅量',
  `library_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '进图书馆次数',
  `library_time_spand` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书馆时长',
  `balance_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡内余额',
  `card_days` int(3) unsigned zerofill DEFAULT '000' COMMENT 'card活跃天数',
  `time6_7costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生的日平均消费',
  `consumetimes11_12` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡充值总额',
  `maxcost7_8` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的最大单笔消费',
  `below10_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '日消费金额小于10天数占比',
  `below2_5_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '单次消费金额小于2.5次数占比',
  `propotion_of_2000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得2000助学金占所有获得学生比例',
  `propotion_of_1500` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1500助学金占所有获得学生比例',
  `scorerank_divided_by_stunum` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名除以学院学生人数',
  `propotion_of_1000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1000助学金占所有获得学生比例',
  `score_rank*consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名乘以消费排名',
  `consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费排名',
  `time7_8consume_avg` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的平均消费',
  `avg_charge` int(3) unsigned zerofill DEFAULT '000' COMMENT '平均充值金额',
  `subsidy` int(3) unsigned zerofill DEFAULT '000' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for students_rank_copy_copy
-- ----------------------------
DROP TABLE IF EXISTS `students_rank_copy_copy`;
CREATE TABLE `students_rank_copy_copy` (
  `student_id` int(10) NOT NULL,
  `score` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名',
  `cost_amount` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费金额',
  `cost_variance` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费方差',
  `cost_avg_day_superMarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_avg_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_avg_day_dinnerHall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_rate_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费在洗衣房占总消费的比例',
  `cost_rate_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天超市消费平均值',
  `cost_times_day_dinnerhall` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天食堂消费平均值',
  `cost_times_day_laundryroom` int(3) unsigned zerofill DEFAULT '000' COMMENT '每天洗衣房消费平均值',
  `cost_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '花费次数',
  `library_borrow` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书借阅量',
  `library_times` int(3) unsigned zerofill DEFAULT '000' COMMENT '进图书馆次数',
  `library_time_spand` int(3) unsigned zerofill DEFAULT '000' COMMENT '图书馆时长',
  `balance_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡内余额',
  `card_days` int(3) unsigned zerofill DEFAULT '000' COMMENT 'card活跃天数',
  `time6_7costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日6点-7点的消费总额',
  `time7_8costs` int(3) unsigned zerofill DEFAULT '000' COMMENT '每日7点-8点的消费总额',
  `totaldinnercosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生日饭堂消费的总额',
  `avgdayscosts` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生的日平均消费',
  `consumetimes11_12` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生每天 11点 - 12点消费的次数',
  `consumetimes0_25` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生单次消费金额在0-2.5元之间的次数',
  `countcost0_10` int(3) unsigned zerofill DEFAULT '000' COMMENT '该学生当日总消费在0-10元范围的天数',
  `cardrecharge` int(3) unsigned zerofill DEFAULT '000' COMMENT '卡充值总额',
  `maxcost7_8` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的最大单笔消费',
  `below10_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '日消费金额小于10天数占比',
  `below2_5_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '单次消费金额小于2.5次数占比',
  `propotion_of_2000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得2000助学金占所有获得学生比例',
  `propotion_of_1500` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1500助学金占所有获得学生比例',
  `scorerank_divided_by_stunum` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名除以学院学生人数',
  `propotion_of_1000` int(3) unsigned zerofill DEFAULT '000' COMMENT '所在学院获得1000助学金占所有获得学生比例',
  `score_rank*consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '成绩排名乘以消费排名',
  `consume_rank` int(3) unsigned zerofill DEFAULT '000' COMMENT '消费排名',
  `time7_8consume_avg` int(3) unsigned zerofill DEFAULT '000' COMMENT '7点 -8点间的平均消费',
  `avg_charge` int(3) unsigned zerofill DEFAULT '000' COMMENT '平均充值金额',
  `subsidy` int(3) unsigned zerofill DEFAULT '000' COMMENT '奖学金额',
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
