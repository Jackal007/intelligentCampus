from a_CalculateField import XXCalculater
from Tools import MyLog

class ConsumeTimes11_12Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select consumetimes11_12 from students order by consumetimes11_12"
        self.executer.execute(sql)
        ConsumeTimes11_12Ranks = self.executer.fetchall()
        A = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.25)][0]
        B = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.5)][0]
        C = ConsumeTimes11_12Ranks[int(len(ConsumeTimes11_12Ranks) * 0.75)][0]
        D = ConsumeTimes11_12Ranks[len(ConsumeTimes11_12Ranks) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生每天 11点 - 12点消费的次数")
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card where student_id=" + studentId + " and hour(deal_date)=11"  
        self.executer.execute(sql)
        s = str(self.executer.fetchone()[0])
        sql = "update students set consumetimes11_12='" + s + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set consumetimes11_12='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
