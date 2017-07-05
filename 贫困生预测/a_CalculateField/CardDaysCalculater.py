from a_CalculateField import XXCalculater
from Tools import MyLog

class CardDaysCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("CardDaysCalculater")
        studentId = self.student.getStudentId()
        sql = "select count(*) from card_2 where studentid=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        dealCost=self.classify(dealCost)
    
        sql = "update students set card_days='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
