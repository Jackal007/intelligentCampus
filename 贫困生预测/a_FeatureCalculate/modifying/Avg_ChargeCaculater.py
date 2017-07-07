from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Below2.5_RankCalculater(XXCalculater.XXCalculater):
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
        print("正在计算各个学生充值平均值")
        studentId = str(self.student.getStudentId())
        sql = "SELECT AVG(deal_cost) AS ChargeAverage FROM card where student_id = "+ studentId+"and deal_type = '卡充值'"
        executer.execute(sql)
        avg = executer.fetchall()
        
        sql = "update students set avg_charge ='" + str(avg) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set avg_charge='" + str(avg) + "' where student_id=" + studentId
        self.executer.execute(sql)