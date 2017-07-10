from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Below10_RankCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select below10_rank from students order by below10_rank"
        self.executer.execute(sql)
        avgDaysCosts = self.executer.fetchall()
        A = avgDaysCosts[int(len(avgDaysCosts) * 0.25)][0]
        B = avgDaysCosts[int(len(avgDaysCosts) * 0.5)][0]
        C = avgDaysCosts[int(len(avgDaysCosts) * 0.75)][0]
        D = avgDaysCosts[len(avgDaysCosts) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
        Below10_RankCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT count(*) from card_2 where studentid = " + studentId + " and date_cost<10.0"
        self.executer.execute(sql)
        below10 = float(self.executer.fetchone()[0])
        sql = "SELECT count(*) from card_2 where studentid = " + studentId
        self.executer.execute(sql)
        allday = float(self.executer.fetchone()[0])
        rank = below10 / allday
        sql = "update students set below10_rank ='" + str(rank) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        Below10_RankCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select below10_rank from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set below10_rank ='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
