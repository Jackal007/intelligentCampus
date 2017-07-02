from a_CalculateField import XXCalculater
from Tools import MyLog

class SubsidyCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("SubsidyCalculater")
        # 对每一个学生统计其奖学金获得情况
        studentId = self.student.getStudentId()
        sql = "select stipend from subsidy where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]

        if subsidy <= self.level["A"]:
            subsidy = "A"
        elif subsidy <= self.level["B"]:
            subsidy = "B"
        elif subsidy <= self.level["C"]:
            subsidy = "C"
        else:
            subsidy = "D"

        sql = "update students set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return subsidy