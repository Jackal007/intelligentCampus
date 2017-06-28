# coding=gbk
'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from MyConfig import AverageCost_level as level

class CalculateCostAverage(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateCostAverage")
        for studentId in tqdm(self.students):
            sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
            self.executer.execute(sql)
            result = self.executer.fetchall()
            for i in result:
                if "dinnerhall" in i[0]:
                    avg_dinnerHall = i[1]
                    if avg_dinnerHall < self.level["A"]:
                        avg_dinnerHall = "A"
                    elif avg_dinnerHall < self.level["B"]:
                        avg_dinnerHall = "B"
                    elif avg_dinnerHall < self.level["C"]:
                        avg_dinnerHall = "C"
                    else:
                        avg_dinnerHall = "D"
                elif "supermarket" in i[0]:
                    avg_superMarket = i[1]
                    if avg_superMarket < self.level["A"]:
                        avg_superMarket = "A"
                    elif avg_superMarket < self.level["B"]:
                        avg_superMarket = "B"
                    elif avg_superMarket < self.level["C"]:
                        avg_superMarket = "C"
                    else:
                        avg_superMarket = "D"
            
            try:
                sql = "update students set cost_avg_dinnerHall='" + str(avg_dinnerHall) + "' where student_id=" + str(studentId) 
                self.executer.execute(sql)
                sql = "update students set cost_avg_superMarket='" + str(avg_superMarket) + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
                self.conn.commit()
#                 sql = "flush query cache"
#                 self.executer.execute(sql)
#                 sql = "flush tables"
#                 self.executer.execute(sql)
#                 self.conn.commit()
            except:
                print(sql)
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostAverage(level)
    t.calculate()
