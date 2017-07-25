from FeatureCalculate import XXCalculater
from Tools import MyLog

class MaxCost7_8Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select maxcost7_8 from students order by maxcost7_8"
        self.executer.execute(sql)
        MaxCost7_8Ranks = self.executer.fetchall()
        A = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.125)][0]
        B = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.25)][0]
        C = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.375)][0]
        D = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.5)][0]
        E = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.625)][0]
        F = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.75)][0]
        G = MaxCost7_8Ranks[int(len(MaxCost7_8Ranks) * 0.875)][0]
        H = MaxCost7_8Ranks[len(MaxCost7_8Ranks) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
        
    @MyLog.myException
    def calculate(self):
        '''
        MaxCost7_8Calculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) as a from card where student_id=" + studentId + " and hour(deal_date)=7  group by date(deal_date) order by a  limit  1"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set maxcost7_8='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        MaxCost7_8Calculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select maxcost7_8 from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set maxcost7_8='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)