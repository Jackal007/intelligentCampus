'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from MyConfig import CostRate_level as level

class CalculateCostRate(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateCostRate")
        for studentId in tqdm(self.students):
            sql = "select deal_way,avg(deal_cost) from card where student_id= " + str(studentId) + " group by deal_way"
            self.executer.execute(sql)
            result = self.executer.fetchall()
            total = 0
            dinnerHall = 0
            superMarket = 0
            for i in result:
                total += i[1]
                if "dinnerhall" in i[0]:
                    dinnerHall = i[1]
                elif "supermarket" in i[0]:
                    superMarket = i[1]
            
            dinnerHall_rate = dinnerHall / total
            if dinnerHall_rate < self.level["A"]:
                dinnerHall_rate = "A"
            elif dinnerHall_rate < self.level["B"]:
                dinnerHall_rate = "B"
            elif dinnerHall_rate < self.level["C"]:
                dinnerHall_rate = "C"
            else:
                dinnerHall_rate = "D"
            superMarket_rate = superMarket / total
            if superMarket_rate < self.level["A"]:
                superMarket_rate = "A"
            elif superMarket_rate < self.level["B"]:
                superMarket_rate = "B"
            elif superMarket_rate < self.level["C"]:
                superMarket_rate = "C"
            else:
                superMarket_rate = "D"
            
            try:
                sql = "update students set cost_avg_dinnerHall='" + dinnerHall_rate + "' where student_id=" + str(studentId) 
                self.executer.execute(sql)
                sql = "update students set cost_avg_superMarket='" + superMarket_rate + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
                self.conn.commit()
            except:
                print(sql)
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostRate(level)
    t.calculate()
