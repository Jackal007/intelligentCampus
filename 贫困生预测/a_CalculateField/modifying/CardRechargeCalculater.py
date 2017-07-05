from a_CalculateField import XXCalculater
from Tools import MyLog

class CardRechargeCalculater(XXCalculater.XXCalculater):
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
        print("正在计算每个学生的卡充值总额")
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId +" and deal_type = '卡充值'"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        
        sql = "update students set  cardrecharge='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        self.conn.commit()
