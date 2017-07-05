from a_CalculateField import XXCalculater
from Tools import MyLog

class AvgDaysCostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 0
        B = 1000
        C = 1500
        D = 2000
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生每日平均消费")
        studentId = str(self.student.getStudentId())
        sql = "select avg(deal_cost) from card where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        
        sql = "update students set avgdayscosts='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
