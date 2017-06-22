'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from LevelConfig import CostAmount_level as level

class CalculateCostAmount(CalculateXX.CalculateXX):

    def calculate(self):
        # 对每一个学生统计其消费金额的情况
        for student in tqdm(self.students):
            student_id = student[0]
            sql = "select count(deal_cost) from card where student_id='" + str(student_id) + "'"
            self.executer.execute(sql)
            deal_cost = self.executer.fetchone()[0]
            weight = 1
            if deal_cost < self.level_1:
                weight *= self.level_1
            elif deal_cost < self.level_2:
                weight *= self.level_2
            else:
                weight *= self.level_3

            sql = "update students set cost_amount='" + str(weight) + "' where student_id='" + str(student_id) + "' "
            self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostAmount(level[0], level[1], level[2], level[3])
    t.calculate()
