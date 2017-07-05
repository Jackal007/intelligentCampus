from a_CalculateField import XXCalculater
from Tools import MyLog

class CountCost0_10Calculater(XXCalculater.XXCalculater):
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
        print("正在计算每个学生当日总消费在0-10元范围的天数")
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card_2 where studentid=" + studentId
        self.executer.execute(sql)
        s = str(self.executer.fetchone()[0])
        
        sql = "update students set countcost0_10='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
        self.conn.commit()
