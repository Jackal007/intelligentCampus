'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from LevelConfig import CostAmount_level as level

class CalculateCostAmount(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateCostAmount")
        # 对每一个学生统计其消费金额的情况
        for student in tqdm(self.students):
            try:
                studentId = student[0]
                sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
                self.executer.execute(sql)
                deal_cost = self.executer.fetchone()[0]
                weight = "C"
                if deal_cost < self.level["A"]:
                    weight = "A"
                elif deal_cost < self.level["B"]:
                    weight ="B"
                else:
                    weight = "C"
    
                sql = "update students set cost_amount='" + str(weight) + "' where student_id='" + str(studentId) + "' "
                self.executer.execute(sql)
            except:
                pass
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostAmount(level)
    t.calculate()
