/*
Navicat MySQL Data Transfer

Source Server         : gdafgadfg
Source Server Version : 50519
Source Host           : localhost:3306
Source Database       : intelligentcampusvalidate

Target Server Type    : MYSQL
Target Server Version : 50519
File Encoding         : 65001

Date: 2017-07-12 17:42:18
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for students_rank
-- ----------------------------
DROP TABLE IF EXISTS `students_rank`;
CREATE TABLE `students_rank` (
  `student_id` int(10) NOT NULL,
  `score` int(3) DEFAULT '0' COMMENT '成绩排名',
  `cost_amount` int(3) DEFAULT '0' COMMENT '花费金额',
  `cost_variance` int(3) DEFAULT '0' COMMENT '消费方差',
  `cost_avg_day_superMarket` int(3) DEFAULT '0' COMMENT '每天超市消费平均值',
  `cost_avg_day_laundryroom` int(3) DEFAULT '0' COMMENT '每天洗衣房消费平均值',
  `cost_avg_day_dinnerHall` int(3) DEFAULT '0' COMMENT '每天食堂消费平均值',
  `cost_rate_supermarket` int(3) DEFAULT '0' COMMENT '花费在超市占总消费的比例',
  `cost_rate_laundryroom` int(3) DEFAULT '0' COMMENT '花费在洗衣房占总消费的比例',
  `cost_rate_dinnerhall` int(3) DEFAULT '0' COMMENT '食堂消费占总消费的比例',
  `cost_times_day_supermarket` int(3) DEFAULT '0' COMMENT '每天超市消费平均值',
  `cost_times_day_dinnerhall` int(3) DEFAULT '0' COMMENT '每天食堂消费平均值',
  `cost_times_day_laundryroom` int(3) DEFAULT '0' COMMENT '每天洗衣房消费平均值',
  `cost_times` int(3) DEFAULT '0' COMMENT '花费次数',
  `library_borrow` int(3) DEFAULT '0' COMMENT '图书借阅量',
  `library_times` int(3) DEFAULT '0' COMMENT '进图书馆次数',
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
  `below10_rank` int(3) DEFAULT '0' COMMENT '日消费金额小于10天数占比',
  `below2.5_rank` int(3) DEFAULT '0' COMMENT '单次消费金额小于2.5次数占比',
  `propotion_of_2000` int(3) DEFAULT '0' COMMENT '所在学院获得2000助学金占所有获得学生比例',
  `propotion_of_1500` int(3) DEFAULT '0' COMMENT '所在学院获得1500助学金占所有获得学生比例',
  `scorerank_divided_by_stunum` int(3) DEFAULT '0' COMMENT '成绩排名除以学院学生人数',
  `propotion_of_1000` int(3) DEFAULT '0' COMMENT '所在学院获得1000助学金占所有获得学生比例',
  `score_rank*consume_rank` int(3) DEFAULT '0' COMMENT '成绩排名乘以消费排名',
  `consume_rank` int(3) DEFAULT '0' COMMENT '消费排名',
  `time7_8consume_avg` int(3) DEFAULT '0' COMMENT '7点 -8点间的平均消费',
  `avg_charge` int(3) DEFAULT '0' COMMENT '平均充值金额',
  `subsidy` int(3) DEFAULT '0' COMMENT '奖学金额',
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of students_rank
-- ----------------------------
