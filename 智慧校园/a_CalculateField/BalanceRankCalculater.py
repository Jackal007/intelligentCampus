from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import BalanceRank_level

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
        averageBalance=self.classify(averageBalance,BalanceRank_level)
            
        sql = "update students set balance_rank='" + averageBalance + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return averageBalance