'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from a_CalculateField.LevelConfig import BookBorrow_level as level

class CalculateLibraryTimeSpand(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateLibraryTimeSpand")
        sql = "insert into library_modify(select student_id,date(date),min(time(date))as entry,max(time(date))as leav,TIMESTAMPDIFF(minute,max(date),min(date)) from library where door_id REGEXP '..[0-6]' group by student_id,date(date))"
        self.executer.execute(sql)
        sql = "SELECT student_id,sum(totaltime) FROM library_modify GROUP BY student_id"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for student in tqdm(students):
            student_id = student[0]
            student_LibraryTime = student[1]

            LibraryTimeRank = ""
            if student_LibraryTime < self.level["A"]:
                LibraryTimeRank = "A"
            elif student_LibraryTime < self.level["B"]:
                LibraryTimeRank = "B"
            else:
                LibraryTimeRank = "C"

            sql = "update students set library_time_spand='" + LibraryTimeRank + "' where student_id='" + str(student_id) + "'"
            self.executer.executer(sql)

        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryTimeSpand(level)
    t.calculate()
