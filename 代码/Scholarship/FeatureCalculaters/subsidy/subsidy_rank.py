'''
Created on 2017年11月21日

@author: qfWu
'''
from Tools import *

class subsidy_rank(FeatureCalculater):
    '''
            计算获得奖学金的等级
    '''
    def setLevel(self):
        pass
        
    @MyLog.myException
    def calculate(self):
        for school_year in self.school_year:
            student_num = str(self.student.getStudentId())
            sql = "SELECT rank FROM subsidy where student_num = " + student_num + " grant_year=" + str(school_year)
            self.executer.execute(sql)
            subsidy_rank = self.executer.fetchone()[0]
            sql = "update students set subsidy_rank ='" + str(subsidy_rank) + "' where student_num=" + student_num + " AND school_year =" + str(school_year)
            self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        pass
