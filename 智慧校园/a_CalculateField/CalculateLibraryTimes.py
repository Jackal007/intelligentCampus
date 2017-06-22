'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from a_CalculateField.LevelConfig import LibraryTimes_level as level

class CalculateLibraryTimes(CalculateXX.CalculateXX):

    def calculate(self):
        print("CalculateLibraryTimes")
        sql="select student_id from students order by score"
        self.executer.execute(sql)
        students = self.executer.fetchall()
        for student in tqdm(students):
            student_id=student[0]

            sql="select count(student_id) from library where student_id='"+str(student_id)+"'"
            self.executer.execute(sql)
            data = self.executer.fetchone()
            study_time=data[0]
            weight=""
            if study_time<self.level["A"]:
                weight="A"
            elif study_time<self.level["B"]:
                weight="B"
            else:
                weight="C"

            sql="update students set library_times='"+str(weight)+"' where student_id='"+str(student_id)+"' "
            self.executer.execute(sql)
        self.conn.commit()
        self.db.close()

if __name__=='__main__':
    t=CalculateLibraryTimes(level)
    t.calculate()
