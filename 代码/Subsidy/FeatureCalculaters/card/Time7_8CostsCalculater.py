from FeatureCalculate import XXCalculater
from Tools import MyLog

class Time7_8CostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select time7_8costs from students order by time6_7costs "
        self.executer.execute(sql)
        Time7_8CostsRanks = self.executer.fetchall()
        A = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.125)][0]
        B = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.25)][0]
        C = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.375)][0]
        D = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.5)][0]
        E = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.625)][0]
        F = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.75)][0]
        G = Time7_8CostsRanks[int(len(Time7_8CostsRanks) * 0.875)][0]
        H = Time7_8CostsRanks[len(Time7_8CostsRanks) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        Time7_8CostsCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId +" and hour(deal_date)=7"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set time7_8costs='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
    
    @MyLog.myException
    def rankit(self):
        '''
        Time7_8CostsCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select time7_8consume_avg from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set time7_8consume_avg = '" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)