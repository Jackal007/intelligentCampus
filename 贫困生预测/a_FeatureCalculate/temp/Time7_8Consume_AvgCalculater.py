from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Time7_8ConsumeCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select Time7_8Consume from students order by Time7_8Consume"
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
        Time7_8ConsumeCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT time7_8costs from students where studentid = " + studentId
        self.executer.execute(sql)
        consume = float(self.executer.fetchone()[0])
        sql = "SELECT count(*) from card_2 where date_cost >0 and studentid = " + studentId
        self.executer.execute(sql)
        allday = float(self.executer.fetchone()[0])
        avg = consume / allday
        sql = "update students set time7_8consume_avg ='" + str(avg) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        Time7_8ConsumeCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select time7_8consume_avg from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update time7_8consume_avg set time7_8consume_avg ='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
