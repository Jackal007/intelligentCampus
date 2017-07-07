from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CountCost0_10Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select countcost0_10 from students order by countcost0_10"
        self.executer.execute(sql)
        CountCost0_10Ranks = self.executer.fetchall()
        A = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.25)][0]
        B = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.5)][0]
        C = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 0.75)][0]
        D = CountCost0_10Ranks[int(len(CountCost0_10Ranks) * 1)-1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生当日总消费在0-10元范围的天数")
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card_2 where studentid=" + studentId
        self.executer.execute(sql)
        s = str(self.executer.fetchone()[0])
        sql = "update students set countcost0_10='" + s + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set countcost0_10='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
