from a_CalculateField import XXCalculater
from Tools import MyLog

class CosumeTimes0_25Calculater(XXCalculater.XXCalculater):
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
        print("正在计算每个学生单次消费金额在0-2.5元之间的次数")
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card where student_id=" + studentId +" and deal_cost between 0 and 2.5"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        
        sql = "update students set  consumetimes0_2.5='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        self.conn.commit()
