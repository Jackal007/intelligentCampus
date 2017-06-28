'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm
from MyConfig import LibraryTimes_level as level
from Tools import MyLog

class CalculateLibraryTimes(CalculateXX.CalculateXX):
    @MyLog.myException
    def calculate(self):
        print("CalculateLibraryTimes")
        for studentId in tqdm(self.students):
            sql="select count(student_id) from library where student_id="+str(studentId)
            self.executer.execute(sql)
            data = self.executer.fetchone()
            studyTimes=data[0]
            weight="D"
            if studyTimes<self.level["A"]:
                weight="A"
            elif studyTimes<self.level["B"]:
                weight="B"
            elif studyTimes<self.level["C"]:
                weight="C"
            try:
                sql="update students set library_times='"+str(weight)+"' where student_id="+str(studentId)
                self.executer.execute(sql)
            except:
                pass
        self.conn.commit()
        self.db.close()

if __name__ == '__main__':
    t = CalculateLibraryTimes(level)
    t.calculate()
