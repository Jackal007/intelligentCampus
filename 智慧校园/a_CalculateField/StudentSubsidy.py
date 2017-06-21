'''
Created on 2017年6月21日

@author: zhenglongtian
'''

import CalculateXX
from tqdm import tqdm

class StudentSubsidy(CalculateXX.CalculateXX):

    def calculate(self):
        sql="select  * from subsidy"
        self.executer.execute(sql)
        students =self.executer.fetchall()
        for student in tqdm(students):

            student_id=student[0]
            subsidy=student[1]

            weight=1
            if int(subsidy)==0:
                weight*=0
            else:
                weight*=1

            sql="insert into students(student_id,can) values('"+str(student_id)+"',"+str(weight)+")"
            try:
                self.executer.execute(sql)
            except:
                pass

        self.conn.commit()
        self.db.close()

if __name__=='__main__':
    t=StudentSubsidy(10,20,30,40)
    t.calculate()
