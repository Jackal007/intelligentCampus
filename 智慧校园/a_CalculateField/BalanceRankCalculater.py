from a_CalculateField import XXCalculater
from Tools import MyLog

class BalanceRankCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("BalanceRankCalculater")
        
        studentId = self.student.getStudentId()
        sql = "select min(balance),max(balance) from card where student_id=" + str(studentId)
        self.executer.execute(sql)
        s = self.executer.fetchone()
        minBalance,maxBalance = s[0],s[1]
        averageBalance = (minBalance + maxBalance) / 2
        
        if averageBalance < self.level["A"]:
            averageBalance = "A"
        elif averageBalance < self.level["B"]:
            averageBalance = "B"
        elif averageBalance < self.level["C"]:
            averageBalance = "C"
        else:
            averageBalance="D"
            
        sql = "update students set balance_rank='" + averageBalance + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return averageBalance