from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CardRechargeCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cardrecharge from students order by cardrecharge"
        self.executer.execute(sql)
        CardRechargeRanks = self.executer.fetchall()
        A = CardRechargeRanks[int(len(CardRechargeRanks) * 0.25)][0]
        B = CardRechargeRanks[int(len(CardRechargeRanks) * 0.5)][0]
        C = CardRechargeRanks[int(len(CardRechargeRanks) * 0.75)][0]
        D = CardRechargeRanks[int(len(CardRechargeRanks) * 1)][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生的卡充值总额")
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId +" and deal_type = '卡充值'"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set cardrecharge='" + str(s) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set cardrecharge='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
