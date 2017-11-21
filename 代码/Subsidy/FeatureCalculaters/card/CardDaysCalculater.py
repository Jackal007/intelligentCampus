from FeatureCalculate import XXCalculater
from Tools import MyLog

class CardDaysCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select card_days from students order by card_days"
        self.executer.execute(sql)
        card_days = self.executer.fetchall()
        A = card_days[int(len(card_days) * 0.125)][0]
        B = card_days[int(len(card_days) * 0.25)][0]
        C = card_days[int(len(card_days) * 0.375)][0]
        D = card_days[int(len(card_days) * 0.5)][0]
        E = card_days[int(len(card_days) * 0.625)][0]
        F = card_days[int(len(card_days) * 0.75)][0]
        G = card_days[int(len(card_days) * 0.875)][0]
        H = card_days[len(card_days) - 1][0]
        self.level = [A, B, C, D, E, F, G]

        
    @MyLog.myException
    def calculate(self):
        '''
        CardDaysCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card_2 where studentid=" + str(studentId) 
        self.executer.execute(sql)
        card_days = self.executer.fetchone()[0]
        sql = "update students set card_days ='" + str(card_days) + "' where student_id=" + studentId
        self.executer.execute(sql)
    
    @MyLog.myException
    def rankit(self):
        '''
        CardDaysCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select card_days from students where student_id=" + studentId   
        self.executer.execute(sql)
        card_days = self.executer.fetchone()[0]
        card_days = self.classify(card_days)
        sql = "update students set card_days='" + card_days + "' where student_id=" + str(studentId)
        self.executer.execute(sql)