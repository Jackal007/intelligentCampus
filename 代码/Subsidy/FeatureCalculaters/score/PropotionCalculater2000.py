from FeatureCalculate import XXCalculater
from Tools import MyLog

class PropotionCalculater2000(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select propotion_of_2000 from students order by propotion_of_2000 "
        self.executer.execute(sql)
        propotion_of_2000 = self.executer.fetchall()
        A = propotion_of_2000[int(len(propotion_of_2000) * 0.125)][0]
        B = propotion_of_2000[int(len(propotion_of_2000) * 0.25)][0]
        C = propotion_of_2000[int(len(propotion_of_2000) * 0.375)][0]
        D = propotion_of_2000[int(len(propotion_of_2000) * 0.5)][0]
        E = propotion_of_2000[int(len(propotion_of_2000) * 0.625)][0]
        F = propotion_of_2000[int(len(propotion_of_2000) * 0.75)][0]
        G = propotion_of_2000[int(len(propotion_of_2000) * 0.875)][0]
        H = propotion_of_2000[len(propotion_of_2000) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        PropotionCalculater2000.rankit
        '''
        sql = "SELECT SUM(2000_num) FROM college_info"
        self.executer.execute(sql)
        sum2000 = self.executer.fetchone()[0]
        
        studentId = str(self.student.getStudentId())
        sql = "select college_id from score where student_id =" + studentId  
        self.executer.execute(sql)
        collegeId = self.executer.fetchone()[0]
        sql = "select 2000_num from college_info where college_id = "+str(collegeId)     
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]/sum2000
        sql = "update students set propotion_of_2000 ='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        PropotionCalculater2000.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select propotion_of_2000 from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set propotion_of_2000 = '" + str(s) + "' where student_id= " + studentId
        self.executer.execute(sql)