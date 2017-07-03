from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostAmount_level

class CostAmountCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostAmountCalculater")
        # 对每一个学生统计其消费金额的情况
        studentId = self.student.getStudentId()
        sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        dealCost=self.classify(dealCost,CostAmount_level)
    
        sql = "update students set cost_amount='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return dealCost
