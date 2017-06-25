'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from MyConfig import Score_level as level

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
            weight = ""
            if int(rank) < T_10:
                weight = "A"
            elif int(rank) < T_30:
                weight = "B"
            else:
                weight = "C"

            sql = "update students set score='" + str(weight) + "' where student_id='" + str(student_id) + "'"
            try:
                self.executer.execute(sql)
            except:
                print(sql)
                continue

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateScore(level)
    t.calculate()
