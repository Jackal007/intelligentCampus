from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class PropotionCalculater2000(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select propotion_of_2000 from students order by propotion_of_2000 "
        self.executer.execute(sql)
        Time6_7CostsRanks = self.executer.fetchall()
        A = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.25)][0]
        B = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.5)][0]
        C = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.75)][0]
        D = Time6_7CostsRanks[len(Time6_7CostsRanks) - 1][0]
        self.level = [A, B, C, D]
        
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