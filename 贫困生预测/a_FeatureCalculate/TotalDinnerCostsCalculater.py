from a_FeatureCalculate import XXCalculater
from Tools import MyLog

class TotalDinnerCostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select totaldinnercosts from students order by totaldinnercosts"
        self.executer.execute(sql)
        TotalDinnerCostsRanks = self.executer.fetchall()
        A = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.25)][0]
        B = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.5)][0]
        C = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.75)][0]
        D = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 1)][0]
        self.level = [A, B, C, D]
    @MyLog.myException
    def calculate(self):
        '''
            TotalDinnerCostsCalculater
        '''
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId + " and deal_way = 'dinnerhall'"
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = str(self.classify(s))
        sql = "update students set  totaldinnercosts='" + s + "' where student_id=" + studentId
        if self.level is not None:
            s = self.classify(s)
            sql = "update students_rank totaldinnercosts='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)
