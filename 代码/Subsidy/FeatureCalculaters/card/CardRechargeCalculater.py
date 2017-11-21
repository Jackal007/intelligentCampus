from FeatureCalculate import XXCalculater
from Tools import MyLog

class CardRechargeCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cardrecharge from students order by cardrecharge"
        self.executer.execute(sql)
        CardRechargeRanks = self.executer.fetchall()
        A = CardRechargeRanks[int(len(CardRechargeRanks) * 0.125)][0]
        B = CardRechargeRanks[int(len(CardRechargeRanks) * 0.25)][0]
        C = CardRechargeRanks[int(len(CardRechargeRanks) * 0.375)][0]
        D = CardRechargeRanks[int(len(CardRechargeRanks) * 0.5)][0]
        E = CardRechargeRanks[int(len(CardRechargeRanks) * 0.625)][0]
        F = CardRechargeRanks[int(len(CardRechargeRanks) * 0.75)][0]
        G = CardRechargeRanks[int(len(CardRechargeRanks) * 0.875)][0]
        H = CardRechargeRanks[len(CardRechargeRanks) - 1][0]
        self.level = [A, B, C, D, E, F, G]
      
        
    @MyLog.myException
    def calculate(self):
        '''
        CardRechargeCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId + " and deal_type = 'charge'"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set cardrecharge='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
            
    @MyLog.myException
    def rankit(self):
        '''
        CardRechargeCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select cardrecharge from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set cardrecharge='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)