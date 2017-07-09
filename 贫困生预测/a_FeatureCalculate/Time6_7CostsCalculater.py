from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class Time6_7CostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select time6_7costs from students order by time6_7costs "
        self.executer.execute(sql)
        Time6_7CostsRanks = self.executer.fetchall()
        A = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.25)][0]
        B = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.5)][0]
        C = Time6_7CostsRanks[int(len(Time6_7CostsRanks) * 0.75)][0]
        D = Time6_7CostsRanks[len(Time6_7CostsRanks) -1][0]
        self.level = [A, B, C, D]
        
    @MyLog.myException
    def calculate(self):
        '''
            Time6_7CostsCalculater
        '''
        studentId = str(self.student.getStudentId())
        if self.level is None:
            sql = "select sum(deal_cost) from card where student_id=" + studentId +" and hour(deal_date)=6"  
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            sql = "update students set time6_7costs='" + str(s) + "' where student_id=" + studentId
            self.executer.execute(sql)
        else:
            sql = "select time6_7costs from students where student_id=" + studentId   
            self.executer.execute(sql)
            s = self.executer.fetchone()[0]
            s = self.classify(s)
            sql = "update students_rank set time6_7costs='" + str(s) + "' where student_id=" + studentId
            self.executer.execute(sql)
