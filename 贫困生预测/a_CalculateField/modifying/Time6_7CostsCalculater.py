from a_CalculateField import XXCalculater
from Tools import MyLog

class Time6_7CostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select as a from card group by student_id order by a"
        self.executer.execute(sql)
        BalanceRanks = self.executer.fetchone()[0]
        A = int(BalanceRanks * 0.25)
        B = int(BalanceRanks * 0.5)
        C = int(BalanceRanks * 0.5)
        D = int(BalanceRanks * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生每日6点-7点的消费总额")
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId +" and hour(deal_date)=6"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        
        sql = "update students set time6_7costs='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        self.conn.commit()
