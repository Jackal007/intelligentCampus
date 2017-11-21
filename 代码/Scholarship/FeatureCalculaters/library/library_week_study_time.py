'''
Created on 2017年11月21日

@author: qfWu
'''
from Tools import *

class library_week_study_time(FeatureCalculater):
    '''
            计算每一学年周末图书馆学习时间
    '''
    def setLevel(self):
        pass
        
    @MyLog.myException
    def calculate(self):
        student_num = str(self.student.getStudentId())
        for school_year in self.school_year:
            sql = "SELECT sum(seat_time) FROM library_study_time where student_num = " + student_num + " AND DAYOFYEAR(select_seat_time)= " + str(school_year) + " AND DAYOFWEEK(select_seat_time) in (6,7)"
            self.executer.execute(sql)
            library_week_study_time = self.executer.fetchone()[0]
            sql = "update students set library_week_study_time ='" + str(library_week_study_time) + "' where student_num=" + student_num + " AND school_year =" + str(school_year)
            self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        pass
