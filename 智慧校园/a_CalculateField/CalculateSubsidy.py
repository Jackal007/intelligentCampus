'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from a_CalculateField.LevelConfig import Subsidy_level as level

class CalculateSubsidy(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateSubsidy")
        # 对每一个学生统计其奖学金获得情况
        for student in tqdm(self.students):
            student_id = student[0]
            subsidy = student[1]

            weight = 1
            if int(subsidy) == 0:
                weight *= 0
            else:
                weight *= 1

            sql = "insert into students(student_id,can) values('" + str(student_id) + "'," + str(weight) + ")"
            try:
                self.executer.execute(sql)
            except:
                pass

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateSubsidy(level[0], level[1], level[2], level[3])
    t.calculate()
