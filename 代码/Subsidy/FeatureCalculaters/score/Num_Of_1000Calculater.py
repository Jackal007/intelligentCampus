from FeatureCalculate import XXCalculater
from Tools import MyLog

class Num_Of_1000Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        pass
        
    @MyLog.myException
    def calculate(self):
        '''
                        正在计算各个学院获得1000助学金数量
        '''
        i = 1
        while i <= 19:
            
            sql ="SELECT count(*) from score LEFT JOIN subsidy ON score.student_id = subsidy.student_id WHERE college_id = "+ str(i)+ " and stipend = 1000"
            self.executer.execute(sql)
            e = self.executer.fetchone()[0]            
            sql="update college_info set 1000_num = "+str(e)+" where college_id ="+str(i)            
            self.executer.execute(sql)
            i = i + 1
            
    @MyLog.myException
    def rankit(self):
        pass