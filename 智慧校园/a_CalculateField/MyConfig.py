'''
Created on 2017年6月21日

@author: zhenglongtian
'''
###### level config ######
# 奖学金额
Subsidy_level = {"A":0, "B":1000, "C": 1500, "D": 2000}
# 成绩排名
Score_level = {"A":10, "B":20, "C":30, "D": 40}
# 消费金额
CostAmount_level = {"A":1500, "B": 3000, "C":5000, "D": 10000}
# ()平均花费
AverageCost_level = {"A":4, "B": 8, "C":12, "D": 20}
# xx消费/总消费比例
CostRate_level = {"A":0.1, "B":0.2, "C":0.3, "D": 0.4}
# 消费次数[not yet]
CostTimes_level = {"A":500, "B": 1000, "C": 2000, "D":1000}
# 借阅书籍数
LibraryBorrow_level = {"A":6, "B":10, "C": 21, "D": 100}
# 图书馆次数
LibraryTimes_level = {"A":50, "B":100, "C":200, "D":500}
# 在图书馆时长
LibraryTimeSpand_level = {"A":60, "B": 90, "C":120, "D": 150}
# 卡内平均余额
BalanceRank_level = {"A":100, "B":200, "C":300, "D":400}
# 消费类型[not yet]
CostType_level = {"A":10, "B":20, "C": 30, "D":40}

###### thread config ######
threadN=50
