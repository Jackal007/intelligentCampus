from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class SubsidyCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select subsidy from students order by subsidy"
        self.executer.execute(sql)
        Subsidy = self.executer.fetchall()
        A = Subsidy[int(len(Subsidy) * 0.25)][0]
        B = Subsidy[int(len(Subsidy) * 0.5)][0]
        C = Subsidy[int(len(Subsidy) * 0.75)][0]
        D = Subsidy[int(len(Subsidy) * 1) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算奖学金获得情况")
        studentId = self.student.getStudentId()
        sql = "select stipend from subsidy where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]
        sql = "update students set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        if self.level is not None:
            subsidy = self.classify(subsidy)
            sql = "update students_rank set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        self.executer.execute(sql)
