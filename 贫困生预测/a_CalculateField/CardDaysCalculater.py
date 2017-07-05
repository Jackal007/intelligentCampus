from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import CostAmount_level

class CardDaysCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CardDaysCalculater")
        # 对每一个学生统计其消费金额的情况
        studentId = self.student.getStudentId()
        sql = "select count(*) from card_2 where studentid=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        dealCost=self.classify(dealCost,CostAmount_level)
    
        sql = "update students set card_days='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return dealCost
