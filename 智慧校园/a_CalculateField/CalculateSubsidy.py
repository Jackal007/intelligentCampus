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
            studentId = student[0]
            sql = "select stipend from subsidy where student_id=" + str(studentId)
            self.executer.execute(sql)
            subsidy = self.executer.fetchone()[0]

            weight = ""
            if int(subsidy) == 0:
                weight = "A"
            else:
                weight = "B"

            sql = "insert into students(student_id,subsidy) values('" + str(studentId) + "','" + weight + "')"
#             try:
            self.executer.execute(sql)
#             except:
#                 pass

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateSubsidy(level)
    t.calculate()
