from FeatureCalculate import XXCalculater
from Tools import MyLog

class PropotionCalculater1500(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select propotion_of_1500 from students order by propotion_of_1000 "
        self.executer.execute(sql)
        propotion_of_1500 = self.executer.fetchall()
        A = propotion_of_1500[int(len(propotion_of_1500) * 0.125)][0]
        B = propotion_of_1500[int(len(propotion_of_1500) * 0.25)][0]
        C = propotion_of_1500[int(len(propotion_of_1500) * 0.375)][0]
        D = propotion_of_1500[int(len(propotion_of_1500) * 0.5)][0]
        E = propotion_of_1500[int(len(propotion_of_1500) * 0.625)][0]
        F = propotion_of_1500[int(len(propotion_of_1500) * 0.75)][0]
        G = propotion_of_1500[int(len(propotion_of_1500) * 0.875)][0]
        H = propotion_of_1500[len(propotion_of_1500) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        PropotionCalculater1500.calculate
        '''
        sql = "SELECT SUM(1500_num) FROM college_info"
        self.executer.execute(sql)
        sum1500 = self.executer.fetchone()[0]
        
        studentId = str(self.student.getStudentId())
        sql = "select college_id from score where student_id =" + studentId  
        self.executer.execute(sql)
        collegeId = self.executer.fetchone()[0]
        sql = "select 1000_num from college_info where college_id = "+str(collegeId)     
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]/sum1500
        sql = "update students set propotion_of_1500 ='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        PropotionCalculater1500.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select propotion_of_1500 from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set propotion_of_1500 = '" + str(s) + "' where student_id= " + studentId
        self.executer.execute(sql)