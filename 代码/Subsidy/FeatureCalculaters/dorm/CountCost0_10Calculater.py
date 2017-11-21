from FeatureCalculate import XXCalculater
from Tools import MyLog

class CountCost0_10Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select countcost0_10 from students order by countcost0_10"
        self.executer.execute(sql)
        CountCost0_10Ranks = self.executer.fetchall()
        A = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.125)][0]
        B = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.25)][0]
        C = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.375)][0]
        D = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.5)][0]
        E = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.625)][0]
        F = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.75)][0]
        G = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.875)][0]
        H = CountCost0_10Ranks[len(CountCost0_10Ranks) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        CountCost0_10Calculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card_2 where studentid=" + studentId
        self.executer.execute(sql)
        s = str(self.executer.fetchone()[0])
        sql = "update students set countcost0_10='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
    
    @MyLog.myException
    def rankit(self):
        '''
        CountCost0_10Calculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select countcost0_10 from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set countcost0_10='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)