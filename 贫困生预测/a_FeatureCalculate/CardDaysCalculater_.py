from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CardDaysCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select card_days from students order by card_days"
        self.executer.execute(sql)
        cardDays = self.executer.fetchone()[0]
        A = int(cardDays * 0.25)
        B = int(cardDays * 0.5)
        C = int(cardDays * 0.5)
        D = int(cardDays * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
            CardDaysCalculater
        '''
        studentId = str(self.student.getStudentId())
        if self.level is None:
            studentId = self.student.getStudentId()
            sql = "select count(*) from card_2 where studentid=" + str(studentId) 
            self.executer.execute(sql)
            dealCost = self.executer.fetchone()[0]
            dealCost = self.classify(dealCost)
            self.executer.execute(sql)
        else:
            sql = "select card_days from students where student_id=" + studentId   
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            dealCost = self.classify(s)
            sql = "update students set card_days='" + dealCost + "' where student_id=" + str(studentId)
            self.executer.execute(sql)
