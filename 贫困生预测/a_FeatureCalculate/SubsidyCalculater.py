from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class SubsidyCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        self.level = [0, 1000, 1500, 2000]
        
    @MyLog.myException
    def calculate(self):
        '''
            SubsidyCalculater
        '''
        studentId = self.student.getStudentId()
        sql = "select stipend from subsidy where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]
        sql = "update students set subsidy= '" + str(subsidy) + "' where student_id = " + str(studentId)
        if self.level is not None:
            subsidy = self.classify(subsidy)
            sql = "update students_rank set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        self.executer.execute(sql)
