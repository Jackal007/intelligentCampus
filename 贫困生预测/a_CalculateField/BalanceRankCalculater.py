from a_CalculateField import XXCalculater
from Tools import MyLog

class BalanceRankCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select (min(balance)+max(balance))/2 as a from card group by student_id order by a"
        self.executer.execute(sql)
        BalanceRanks = self.executer.fetchone()[0]
        A = int(BalanceRanks * 0.25)
        B = int(BalanceRanks * 0.5)
        C = int(BalanceRanks * 0.5)
        D = int(BalanceRanks * 1)
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算卡内余额")
        studentId = str(self.student.getStudentId())
        sql = "select min(balance),max(balance) from card where student_id=" + studentId
        self.executer.execute(sql)
        s = self.executer.fetchone()
        minBalance, maxBalance = s[0], s[1]
        
        averageBalance = (minBalance + maxBalance) / 2
        averageBalance = str(self.classify(averageBalance))
            
        sql = "update students set balance_rank='" + averageBalance + "' where student_id=" + studentId
        self.executer.execute(sql)
