'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from a_CalculateField.LevelConfig import BookBorrow_level as level

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
            student_id = list[0]
            supermarket = 0.0
            dinnerHall = 0.0
            for student in students:
                if student[0] == student_id and student[1] == '食堂':
                    dinnerHall = student[2] / list[1]
                if student[0] == student_id and student[1] == '超市':
                    supermarket = student[2] / list[1]
                sql = "update students set cost_avg_dinnerHall='" + str(dinnerHall) + "' where student_id='" + str(student_id) + "' "
                self.executer.execute(sql)
                sql = "update students set cost_supermarket_rate='" + str(supermarket) + "' where student_id='" + str(student_id) + "' "
                self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostRate(level)
    t.calculate()
