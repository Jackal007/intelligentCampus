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
        print("正在计算各个学生单笔消费0~2.5元笔数占比")
        studentId = str(self.student.getStudentId())
        sql = "SELECT count(*) from card where student_id = "+ studentId
        executer.execute(sql)
        all = executer.fetchall()
        
        sql = "SELECT count(*) from card where student_id = "+ studentId+"and deal_cost > 0 and deal_cost<2.5"  
        self.executer.execute(sql)
        below2.5 = self.executer.fetchall()
        
        rank = below2.5/all
        sql = "update students set  ='" + str(rank) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set Below_2.5_Rank='" + str(rank) + "' where student_id=" + studentId
        self.executer.execute(sql)