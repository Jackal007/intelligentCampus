from a_CalculateField import XXCalculater
from Tools import MyLog

class CostAmountCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 90
        B = 120
        C = 150
        D = 180
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("CostAmountCalculater")
        studentId = self.student.getStudentId()
        sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        dealCost=self.classify(dealCost)
    
        sql = "update students set cost_amount='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return dealCost
