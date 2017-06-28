'''
Created on 2017年6月21日

@author: zhenglongtian
'''

from tqdm import tqdm
import CalculateXX
from MyConfig import CostTimes_level as level

class CalculateLibraryBorrow(CalculateXX.CalculateXX):

    def calculate(self):
        
        print("CalculateLibraryBorrow")
        # 对每一个学生统计其消费次数
        for studentId in tqdm(self.students):
            sql = "select count(*) from card where student_id=" + str(studentId)
            self.executer.execute(sql)

            data = self.executer.fetchone()
            cost_times = data[0]
            weight = "D"
            if cost_times < self.level["A"]:
                weight ="A"
            elif cost_times < self.level["B"]:
                weight ="B"
            elif cost_times < self.level["C"]:
                weight = "C"

            sql = "update students set cost_times='" + str(weight) + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryBorrow(level)
    t.calculate()
