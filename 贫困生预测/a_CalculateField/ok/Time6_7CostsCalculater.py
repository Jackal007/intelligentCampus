from a_CalculateField import XXCalculater
from Tools import MyLog

class Time6_7CostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 0
        B = 1000
        C = 1500
        D = 2000
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生每日6点-7点的消费总额")
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId +" and hour(deal_date)=6"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s=self.classify(s)
        
        sql = "update students set time6_7costs='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        self.conn.commit()
