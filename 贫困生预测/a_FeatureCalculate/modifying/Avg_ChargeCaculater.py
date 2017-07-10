from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Avg_ChargeCaculater(XXCalculater.XXCalculater):
    '''
    Avg_ChargeCaculater
    '''
    def setLevel(self):
        sql = "select avg_charge from students order by avg_charge"
        self.executer.execute(sql)
        avgDaysCosts = self.executer.fetchall()
        A = avgDaysCosts[int(len(avgDaysCosts) * 0.25)][0]
        B = avgDaysCosts[int(len(avgDaysCosts) * 0.5)][0]
        C = avgDaysCosts[int(len(avgDaysCosts) * 0.75)][0]
        D = avgDaysCosts[int(len(avgDaysCosts)) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        studentId = str(self.student.getStudentId())
        sql = "SELECT AVG(deal_cost) FROM card where student_id = "+ studentId+"and deal_type = '卡充值'"
        self.executer.execute(sql)
        avg = self.executer.fetchone()[0]
        sql = "update students set avg_charge ='" + str(avg) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        studentId = str(self.student.getStudentId())
        sql = "select avg_charge from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set avg_charge='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)