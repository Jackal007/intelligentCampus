from a_CalculateField import XXCalculater
from Tools import MyLog

class BalanceRankCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select balance_rank from students order by balance_rank"
        self.executer.execute(sql)
        BalanceRanks = self.executer.fetchall()
        A = BalanceRanks[int(len(BalanceRanks) * 0.25)][0]
        B = BalanceRanks[int(len(BalanceRanks) * 0.5)][0]
        C = BalanceRanks[int(len(BalanceRanks) * 0.75)][0]
        D = BalanceRanks[len(BalanceRanks) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算卡内余额")
        studentId = str(self.student.getStudentId())
        sql = "select min(balance),max(balance) from card where student_id=" + studentId
        self.executer.execute(sql)
        s = self.executer.fetchone()
        minBalance, maxBalance = s[0], s[1]
        averageBalance = str((minBalance + maxBalance) / 2)
        sql = "update students set balance_rank='" + averageBalance + "' where student_id=" + studentId
        if self.level is not None:
            averageBalance = self.classify(s)
            sql = "update students_rank set balance_rank='" + averageBalance + "' where student_id=" + studentId
        self.executer.execute(sql)
