from FeatureCalculate import XXCalculater
from Tools import MyLog

class scorerank_divided_by_stunum(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select scorerank_divided_by_stunum from students order by scorerank_divided_by_stunum "
        self.executer.execute(sql)
        scorerank_divided_by_stunum = self.executer.fetchall()
        A = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.125)][0]
        B = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.25)][0]
        C = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.375)][0]
        D = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.5)][0]
        E = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.625)][0]
        F = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.75)][0]
        G = scorerank_divided_by_stunum[int(len(scorerank_divided_by_stunum) * 0.875)][0]
        H = scorerank_divided_by_stunum[len(scorerank_divided_by_stunum) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        scorerank_divided_by_stunum.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT rank FROM score where student_id = "+ studentId
        self.executer.execute(sql)
        rank = self.executer.fetchone()[0]
        sql = "select college_id from score where student_id =" + studentId  
        self.executer.execute(sql)
        collegeId = self.executer.fetchone()[0]
        sql = "select stu_num from college_info where college_id = "+str(collegeId)     
        self.executer.execute(sql)
        stu_num = self.executer.fetchone()[0]
        s = rank/stu_num
        sql = "update students set scorerank_divided_by_stunum ='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        scorerank_divided_by_stunum.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select scorerank_divided_by_stunum from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set scorerank_divided_by_stunum = '" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)