from FeatureCalculate import XXCalculater
from Tools import MyLog

class ConsumeTimes11_12Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select consumetimes11_12 from students order by consumetimes11_12"
        self.executer.execute(sql)
        
        ConsumeTimes11_12Ranks = self.executer.fetchall()
        A = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.125)][0]
        B = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.25)][0]
        C = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.375)][0]
        D = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.5)][0]
        E = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.625)][0]
        F = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.75)][0]
        G = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.875)][0]
        H = ConsumeTimes11_12Ranks[len(ConsumeTimes11_12Ranks) - 1][0]
        self.level = [A, B, C, D, E, F, G]

    @MyLog.myException
    def calculate(self):
        '''
        ConsumeTimes11_12Calculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card where student_id=" + studentId + " and hour(deal_date)=11"  
        self.executer.execute(sql)
        s = str(self.executer.fetchone()[0])
        sql = "update students set consumetimes11_12='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
            
    @MyLog.myException
    def rankit(self):
        '''
        ConsumeTimes11_12Calculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select consumetimes11_12 from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set consumetimes11_12='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)