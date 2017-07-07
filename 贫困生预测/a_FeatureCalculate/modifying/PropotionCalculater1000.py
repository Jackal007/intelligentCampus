from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class PropotionCalculater1000(XXCalculater.XXCalculater):
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
        print("正在计算该学生所在学院获得1000助学金占比")
        sql = "SELECT SUM(1000_propotion) FROM college_info"
        executer.execute(sql)
        sum1000 = executer.fetchall()
        studentId = str(self.student.getStudentId())
        sql = "select college_id from score where student_id =" + studentId  
        self.executer.execute(sql)
        collegeId = self.executer.fetchall()
        sql = "select 1000_num from college_info where college_id = "+collegeId     
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]/sum1000
        sql = "update students set 1000_propotion ='" + str(s) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students set 1000_propotion ='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)