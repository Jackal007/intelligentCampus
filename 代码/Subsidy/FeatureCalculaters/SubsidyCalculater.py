from FeatureCalculate import XXCalculater
from Tools import MyLog

class SubsidyCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        self.level = [0, 1000, 1500, 2000]
        
    @MyLog.myException
    def calculate(self):
        '''
        SubsidyCalculater.calculate
        '''
        studentId = self.student.getStudentId()
        sql = "select stipend from subsidy where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]
        sql = "update students set subsidy= '" + str(subsidy) + "' where student_id = " + str(studentId)
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        ScoreRankCalculater.rankit
        '''
        studentId = self.student.getStudentId()
        sql = "select subsidy from students where student_id=" + str(studentId)
        self.executer.execute(sql)
        subsidy = self.executer.fetchone()[0]
        subsidy = self.classify(subsidy)
        sql = "update students_rank set subsidy= '" + subsidy + "' where student_id = " + str(studentId)
        self.executer.execute(sql)  