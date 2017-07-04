from a_CalculateField import XXCalculater
from Tools import MyLog
from MyConfig import Subsidy_level

class SubsidyCalculater(XXCalculater.XXCalculater):
    @MyLog.myException
    def calculate(self):
        print("SubsidyCalculater")
        # 对每一个学生统计其奖学金获得情况
        studentId = self.student.getStudentId()
        sql = "select stipend from subsidy where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]

        subsidy = self.classify(subsidy, Subsidy_level)

        sql = "update students set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        self.executer.execute(sql)
        self.conn.commit()
        return subsidy
