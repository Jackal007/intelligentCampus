from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class AvgDaysCostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select avgdayscosts from students order by avgdayscosts"
        self.executer.execute(sql)
        avgDaysCosts = self.executer.fetchall()
        A = avgDaysCosts[int(len(avgDaysCosts) * 0.25)][0]
        B = avgDaysCosts[int(len(avgDaysCosts) * 0.5)][0]
        C = avgDaysCosts[int(len(avgDaysCosts) * 0.75)][0]
        D = avgDaysCosts[int(len(avgDaysCosts)) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
            AvgDaysCostsCalculater
        '''
        studentId = str(self.student.getStudentId())
        sql = "select avg(deal_cost) from card where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set avgdayscosts='" + str(s) + "' where student_id=" + studentId
        
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set avgdayscosts='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
