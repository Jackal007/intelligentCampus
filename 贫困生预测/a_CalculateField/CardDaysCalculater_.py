from a_CalculateField import XXCalculater
from Tools import MyLog

class CardDaysCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select count(*)as a from card_2 group by studentid order by a"
        self.executer.execute(sql)
        cardDays = self.executer.fetchone()[0]
        A = int(cardDays * 0.25)
        B = int(cardDays * 0.5)
        C = int(cardDays * 0.5)
        D = int(cardDays * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("CardDaysCalculater")
        studentId = self.student.getStudentId()
        sql = "select count(*) from card_2 where studentid=" + str(studentId) 
        self.executer.execute(sql)
        dealCost = self.executer.fetchone()[0]
        dealCost = self.classify(dealCost)
    
        sql = "update students set card_days='" + dealCost + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
