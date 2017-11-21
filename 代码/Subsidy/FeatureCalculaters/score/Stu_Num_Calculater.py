from FeatureCalculate import XXCalculater
from Tools import MyLog

class Stu_Num_Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        pass
        
    @MyLog.myException
    def calculate(self):
        i = 1
        while i <= 19:
            
            sql ="SELECT count(*) from score WHERE college_id = "+ str(i)
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            
            sql="update college_info set stu_num = "+str(s)+" where college_id ="+str(i)
            print(sql)
            self.executer.execute(sql)
            i = i + 1
