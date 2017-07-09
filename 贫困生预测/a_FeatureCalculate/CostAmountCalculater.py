from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CostAmountCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_amount from students order by cost_amount"
        self.executer.execute(sql)
        CostAmounts = self.executer.fetchall()
        A = CostAmounts[int(len(CostAmounts) * 0.25)][0]
        B = CostAmounts[int(len(CostAmounts) * 0.5)][0]
        C = CostAmounts[int(len(CostAmounts) * 0.75)][0]
        D = CostAmounts[len(CostAmounts) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
            CostAmountCalculater
        '''
        studentId = str(self.student.getStudentId())
        if self.level is None:
            sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            sql = "update students set cost_amount='" + str(s) + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
        else:
            sql = "select cost_amount from students where student_id=" + studentId   
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            s = self.classify(s)
            sql = "update students_rank set cost_amount='" + s + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
