from a_CalculateField import XXCalculater
from Tools import MyLog

class CostAmountCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select sum(deal_cost) as c from card group by student_id order by c"
        self.executer.execute(sql)
        CostAmounts = self.executer.fetchall()
        A = CostAmounts[int(len(CostAmounts) * 0.25)][0]
        B = CostAmounts[int(len(CostAmounts) * 0.5)][0]
        C = CostAmounts[int(len(CostAmounts) * 0.75)][0]
        D = CostAmounts[int(len(CostAmounts) * 1) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("CostAmountCalculater")
        studentId = self.student.getStudentId()
        sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        dealCost = self.classify(dealCost)
    
        sql = "update students set cost_amount='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
