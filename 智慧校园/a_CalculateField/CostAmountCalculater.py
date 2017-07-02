from a_CalculateField import XXCalculater
from Tools import MyLog

class CostAmountCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CostAmountCalculater")
        # 对每一个学生统计其消费金额的情况
        studentId = self.student.getStudentId()
        sql = "select sum(deal_cost) from card where student_id=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        if dealCost < self.level["A"]:
            dealCost = "A"
        elif dealCost < self.level["B"]:
            dealCost = "B"
        elif dealCost < self.level["C"]:
            dealCost = "C"
        else:
            dealCost = "D"
    
        sql = "update students set cost_amount='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return dealCost
