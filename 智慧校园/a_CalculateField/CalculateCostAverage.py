'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from a_CalculateField.LevelConfig import AverageCost_level as level

class CalculateCostAverage(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateCostAverage")
        sql = "select student_id,deal_way,avg(deal_cost) from card group by student_id,deal_way"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        avg_dinnerHall=""
        avg_superMarket=""
        for student in tqdm(students):
            student_id = student[0]
            if student[1] == "食堂":
                avg_dinnerHall = student[2]
            if student[1] == "超市":
                avg_superMarket = student[2]
            sql = "update students set cost_avg_dinnerHall='" + str(avg_dinnerHall) + "' where student_id='" + str(student_id) + "' "
            self.executer.execute(sql)
            sql = "update students set cost_avg_superMarket='" + str(avg_superMarket) + "' where student_id='" + str(student_id) + "' "
            self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateCostAverage(level)
    t.calculate()
