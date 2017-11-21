from FeatureCalculate import XXCalculater
from Tools import MyLog

class Time7_8Consume_Avg(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select time7_8costs from students order by time7_8costs"
        self.executer.execute(sql)
        Time7_8Consume_Avg = self.executer.fetchall()
        A = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.125)][0]
        B = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.25)][0]
        C = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.375)][0]
        D = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.5)][0]
        E = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.625)][0]
        F = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.75)][0]
        G = Time7_8Consume_Avg[int(len(Time7_8Consume_Avg) * 0.875)][0]
        H = Time7_8Consume_Avg[len(Time7_8Consume_Avg) - 1][0]
        self.level = [A, B, C, D, E, F, G]
       
        
    @MyLog.myException
    def calculate(self):
        '''
        Time7_8Consume_Avg.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) as a from card where student_id=" + studentId + " and hour(deal_date)=7  group by date(deal_date) order by a  limit  1"  
        self.executer.execute(sql)
        
        s = self.executer.fetchone()[0]
        sql = "update students set time7_8consume_avg ='" + str(s) + "' where student_id=" + studentId
        
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        Time7_8Consume_Avg.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select time7_8consume_avg from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set time7_8consume_avg = '" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)