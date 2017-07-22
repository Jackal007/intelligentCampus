from FeatureCalculate import XXCalculater
from Tools import MyLog

class PropotionCalculater1000(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select propotion_of_1000 from students order by propotion_of_1000 "
        self.executer.execute(sql)
        propotion_of_1000 = self.executer.fetchall()
        A = propotion_of_1000[int(len(propotion_of_1000) * 0.25)][0]
        B = propotion_of_1000[int(len(propotion_of_1000) * 0.5)][0]
        C = propotion_of_1000[int(len(propotion_of_1000) * 0.75)][0]
        D = propotion_of_1000[len(propotion_of_1000) - 1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
        PropotionCalculater1000.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT SUM(1000_num) FROM college_info"
        self.executer.execute(sql)
        sum1000 = self.executer.fetchone()[0]
        sql = "select college_id from score where student_id =" + studentId  
        self.executer.execute(sql)
        collegeId = self.executer.fetchone()[0]
        sql = "select 1000_num from college_info where college_id = "+str(collegeId)     
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]/sum1000
        sql = "update students set propotion_of_1000 ='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        PropotionCalculater1000.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select propotion_of_1000 from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set propotion_of_1000 = '" + str(s) + "' where student_id= " + studentId
        self.executer.execute(sql)