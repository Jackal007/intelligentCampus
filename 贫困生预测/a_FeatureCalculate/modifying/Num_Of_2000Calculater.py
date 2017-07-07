from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Num_Of_2000Calculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select time6_7costs from students order by time6_7costs "
        self.executer.execute(sql)
        Time6_7CostsRanks = self.executer.fetchall()
        A = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.25)][0]
        B = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.5)][0]
        C = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.75)][0]
        D = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 1)][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        print("正在计算各个学院获得2000助学金数量")
        i = 1
        while i <= 19:
            
            sql ="SELECT count(*) from score LEFT JOIN subsidy ON score.student_id = subsidy.student_id WHERE college_id = "+ str(i)+ "and stipend = 2000"
            executer.execute(sql)
            e = executer.fetchall()
            
            sql="update college_info set 2000_num = "+str(e)+"where college_id ="+str(i)
            if self.level is not None:
                s = self.classify(s)
                sql="update college_info set 2000_num = "+str(e)+"where college_id ="+str(i)
                self.executer.execute(sql)
            i = i + 1
