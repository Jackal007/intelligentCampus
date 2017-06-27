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
            avg_dinnerHall="C"
            avg_superMarket="C"
            sql = "select deal_way,avg(deal_cost) from card where student_id= "+str(studentId)+" group by deal_way"
            self.executer.execute(sql)
            result = self.executer.fetchall()
            for i in result:
                if i[0]=="食堂":
                    avg_dinnerHall = i[1]
                    if avg_dinnerHall < self.level["A"]:
                        avg_dinnerHall ="A"
                    elif avg_dinnerHall < self.level["B"]:
                        avg_dinnerHall ="B"
                    else:
                        avg_dinnerHall = "C"
                elif i[0]=="超市":
                    avg_superMarket = i[1]
                    if avg_superMarket < self.level["A"]:
                        avg_superMarket ="A"
                    elif avg_superMarket < self.level["B"]:
                        avg_superMarket ="B"
                    else:
                        avg_superMarket = "C"
            
            sql = "update students set cost_avg_dinnerHall='" + str(avg_dinnerHall) + "' where student_id='" + str(studentId) + "' "
            self.executer.execute(sql)
            sql = "update students set cost_avg_superMarket='" + str(avg_superMarket) + "' where student_id='" + str(studentId) + "' "
            self.executer.execute(sql)
            self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostAverage(level)
    t.calculate()
