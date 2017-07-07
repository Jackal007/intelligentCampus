from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Below10_RankCalculater(XXCalculater.XXCalculater):
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
        print("正在计算各个学生日消费小于10天数占比")
        studentId = str(self.student.getStudentId())
        sql = "SELECT count(*) from card_2 where studentid = "+ studentId+"and date_cost<10.0"
        executer.execute(sql)
        below10 = executer.fetchall()
        
        sql = "SELECT count(*) from card_2 where studentid = "+ studentId  
        self.executer.execute(sql)
        allday = self.executer.fetchall()
        
        rank = below10/allday
        sql = "update students set below10_rank ='" + str(rank) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set below10_rank ='" + str(rank) + "' where student_id=" + studentId
        self.executer.execute(sql)