from a_CalculateField import XXCalculater
from Tools import MyLog

class scorerank_divided_by_stunum(XXCalculater.XXCalculater):
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
        print("正在计算学生排名占比")
        studentId = str(self.student.getStudentId())
        sql = "SELECT rank FROM score where student_id = "+ studentId
        executer.execute(sql)
        rank = executer.fetchall()
        
        sql = "select college_id from score where student_id =" + studentId  
        self.executer.execute(sql)
        collegeId = self.executer.fetchall()
        sql = "select stu_num from college_info where college_id = "+collegeId     
        self.executer.execute(sql)
        stu_num = self.executer.fetchone()[0]
        s = rank/stu_num
        sql = "update students set scorerank_divided_by_stunum ='" + str(s) + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank set scorerank_divided_by_stunum='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)