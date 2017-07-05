from a_CalculateField import XXCalculater
from Tools import MyLog

class SubsidyCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        A = 0
        B = 1000
        C = 1500
        D = 2000
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算奖学金获得情况")
        studentId = self.student.getStudentId()
        sql = "select stipend from subsidy where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]

        subsidy = self.classify(subsidy)

        sql = "update students set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        self.executer.execute(sql)
