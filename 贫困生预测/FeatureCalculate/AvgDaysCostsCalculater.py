from FeatureCalculate import XXCalculater
from Tools import MyLog

class AvgDaysCostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select avgdayscosts from students order by avgdayscosts"
        self.executer.execute(sql)
        avgDaysCosts = self.executer.fetchall()
        A = avgDaysCosts[int(len(avgDaysCosts) * 0.125)][0]
        B = avgDaysCosts[int(len(avgDaysCosts) * 0.25)][0]
        C = avgDaysCosts[int(len(avgDaysCosts) * 0.375)][0]
        D = avgDaysCosts[int(len(avgDaysCosts) * 0.5)][0]
        E = avgDaysCosts[int(len(avgDaysCosts) * 0.625)][0]
        F = avgDaysCosts[int(len(avgDaysCosts) * 0.75)][0]
        G = avgDaysCosts[int(len(avgDaysCosts) * 0.875)][0]
        H = avgDaysCosts[len(avgDaysCosts) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        AvgDaysCostsCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select avg(deal_cost) from card where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set avgdayscosts='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        AvgDaysCostsCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select avgdayscosts from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set avgdayscosts='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
