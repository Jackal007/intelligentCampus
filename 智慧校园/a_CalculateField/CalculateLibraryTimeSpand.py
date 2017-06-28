'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from MyConfig import LibraryTimeSpand_level as level

class CalculateLibraryTimeSpand(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateLibraryTimeSpand")
        sql = "insert into library_modify(select student_id,date(date),min(time(date)),max(time(date)),TIMESTAMPDIFF(minute,min(date),max(date)) from library  group by student_id,date(date))"
        self.executer.execute(sql)
        sql = "SELECT student_id,sum(totaltime) FROM library_modify GROUP BY student_id"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for student in tqdm(students):
            studentId = student[0]
            student_LibraryTime = student[1]

            LibraryTimeRank = "D"
            if student_LibraryTime < self.level["A"]:
                LibraryTimeRank = "A"
            elif student_LibraryTime < self.level["B"]:
                LibraryTimeRank = "B"
            elif student_LibraryTime < self.level["C"]:
                LibraryTimeRank = "C"
                
            try:
                sql = "update students set library_time_spand='" + LibraryTimeRank + "' where student_id=" + str(studentId)
                self.executer.execute(sql)
            except:
                pass
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryTimeSpand(level)
    t.calculate()
