from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Time6_7CostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select time6_7costs from students order by time6_7costs "
        self.executer.execute(sql)
        Time6_7CostsRanks = self.executer.fetchall()
        A = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.25)][0]
        B = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.5)][0]
        C = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.75)][0]
        D = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 1)][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生每日6点-7点的消费总额")
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId +" and hour(deal_date)=6"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set time6_7costs='" + str(s) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set time6_7costs='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
