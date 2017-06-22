'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from a_CalculateField.LevelConfig import BookBorrow_level as level

class CalculateScore(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateScore")
        countSQL = "select max(rank) from score"
        studentSQL = "select * from score"

        self.executer.execute(countSQL)
        studentNum = self.executer.fetchone()[0]
        T_10 = int(studentNum * 0.1)
        T_30 = int(studentNum * 0.3)
        T_50 = int(studentNum * 0.5)

        self.executer.execute(studentSQL)
        students = self.executer.fetchall()

        for student in tqdm(students):
            student_id = student[0]
            rank = student[2]
            weight = 1
            if int(rank) < T_10:
                weight *= self.level_1
#                 print(str(10)+"   "+str(rank))
            elif int(rank) < T_30:
                weight *= self.level_2
#                 print(str(30)+"   "+str(rank))
            elif int(rank) < T_50:
                weight *= self.level_3
#                 print(str(50)+"   "+str(rank))
            else:
                weight *= self.level_4
#                 print(str(rank))

            sql = "update students set score='" + str(weight) + "' where student_id='" + str(student_id) + "'"
            try:
                self.executer.execute(sql)
            except:
                print(sql)
                continue

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateScore(level[0], level[1], level[2], level[3])
    t.calculate()
