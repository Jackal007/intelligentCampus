'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from a_CalculateField.LevelConfig import BookBorrow_level as level

class CalculateLibraryTimeSpand(CalculateXX.CalculateXX):

    def calculate(self):
        sql = "insert into library_modify(select f1,date(f3),min(time(f3))as entry,max(time(f3))as leav,TIMESTAMPDIFF(minute,max(f3),min(f3)) from library_trainwhere f2 REGEXP '..[0-6]' group by f1,date(f3))"
        self.executer.execute(sql)
        sql = "SELECT student_id,sum(totaltime) FROM library_modify GROUP BY student_id"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for student in tqdm(students):
            student_id = student[0]
            student_LibraryTime = student[1]

            LibraryTimeRank = -1
            if student_LibraryTime < 300:
                LibraryTimeRank = 1
            elif student_LibraryTime < 600:
                LibraryTimeRank = 2
            elif student_LibraryTime < 900:        
                LibraryTimeRank = 3
            elif student_LibraryTime < 1800:
                LibraryTimeRank = 4
            else:
                LibraryTimeRank = 5

            sql = "update students set LibraryTimeRank='" + LibraryTimeRank + "' where student_id='" + str(student_id) + "'"
            self.executer.executer(sql)

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryTimeSpand(level[0], level[1], level[2], level[3])
    t.calculate()
