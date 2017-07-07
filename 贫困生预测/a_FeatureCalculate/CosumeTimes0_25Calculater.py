from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class CosumeTimes0_25Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select consumetimes0_25 from students order by consumetimes0_25"
        self.executer.execute(sql)
        CosumeTimes0_25Ranks = self.executer.fetchall()
        A = CosumeTimes0_25Ranks[int(len(CosumeTimes0_25Ranks) * 0.25)][0]
        B = CosumeTimes0_25Ranks[int(len(CosumeTimes0_25Ranks) * 0.5)][0]
        C = CosumeTimes0_25Ranks[int(len(CosumeTimes0_25Ranks) * 0.75)][0]
        D = CosumeTimes0_25Ranks[int(len(CosumeTimes0_25Ranks) * 1) - 1 ][0]
        self.level = [A, B, C, D]
        
        
    @MyLog.myException
    def calculate(self):
        print("正在计算每个学生单次消费金额在0-2.5元之间的次数")
        studentId = str(self.student.getStudentId())
        sql = "select count(*) from card where student_id=" + studentId + " and deal_cost between 0 and 2.5"  
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set consumetimes0_25 ='" + str(s) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set consumetimes0_25 ='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
