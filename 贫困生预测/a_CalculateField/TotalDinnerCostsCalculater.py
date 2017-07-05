from a_CalculateField import XXCalculater
from Tools import MyLog

class TotalDinnerCostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 1
        B = 2
        C = 3
        D = 499
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生饭堂消费总额")
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId + " and deal_way = 'dinnerhall'"
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = str(self.classify(s))
        if s is not None:
            print(s)
            sql = "update students set  totaldinnercosts='" + s + "' where student_id=" + studentId
            self.executer.execute(sql)
