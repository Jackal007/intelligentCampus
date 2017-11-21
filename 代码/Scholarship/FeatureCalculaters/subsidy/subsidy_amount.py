'''
Created on 2017年11月21日

@author: qfWu
'''
from Tools import *

class subsidy_amount(FeatureCalculater):
    '''
            计算获得奖学金的金额
    '''
    def setLevel(self):
        pass
        
    @MyLog.myException
    def calculate(self):
        for school_year in self.school_year:
            student_num = str(self.student.getStudentId())
            sql = "SELECT amount FROM subsidy where student_num = " + student_num + " grant_year=" + str(school_year)
            self.executer.execute(sql)
            subsidy_amount = self.executer.fetchone()[0]
            sql = "update students set subsidy_amount ='" + str(subsidy_amount) + "' where student_num=" + student_num + " AND school_year =" + str(school_year)
            self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        pass
