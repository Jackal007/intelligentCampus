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
        sql = "select student_id,sum(deal_cost) from card group by student_id"
        self.executer.execute(sql)
        lists = self.executer.fetchall()
        sql = "select student_id,deal_way,sum(deal_cost) from card group by student_id,deal_way"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for list in tqdm(lists):
            studentId = list[0]
            for student in students:
                supermarket = "D"
                dinnerHall = "D"
                if student[0] == studentId and student[1] == '食堂':
                    dinnerHall = student[2] / list[1]
                    if dinnerHall < self.level["A"]:
                        dinnerHall = "A"
                    elif dinnerHall < self.level["B"]:
                        dinnerHall = "B"
                    else:
                        dinnerHall = "C"
                
                if student[0] == studentId and student[1] == '超市':
                    supermarket = student[2] / list[1]
                    if supermarket < self.level["A"]:
                        supermarket = "A"
                    elif supermarket < self.level["B"]:
                        supermarket = "B"
                    else:
                        supermarket = "C"
                sql = "update students set cost_dinnerhall_rate='" + str(dinnerHall) + "' where student_id='" + str(studentId) + "' "
                self.executer.execute(sql)
                sql = "update students set cost_supermarket_rate='" + str(supermarket) + "' where student_id='" + str(studentId) + "' "
                self.executer.execute(sql)
                print("one over")
                self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostRate(level)
    t.calculate()
