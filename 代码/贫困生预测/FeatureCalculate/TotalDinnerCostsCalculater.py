from FeatureCalculate import XXCalculater
from Tools import MyLog

class TotalDinnerCostsCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select totaldinnercosts from students order by totaldinnercosts"
        self.executer.execute(sql)
        TotalDinnerCostsRanks = self.executer.fetchall()
        A = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.125)][0]
        B = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.25)][0]
        C = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.375)][0]
        D = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.5)][0]
        E = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.625)][0]
        F = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.75)][0]
        G = TotalDinnerCostsRanks[int(len(TotalDinnerCostsRanks) * 0.875)][0]
        H = TotalDinnerCostsRanks[len(TotalDinnerCostsRanks) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        TotalDinnerCostsCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "select sum(deal_cost) from card where student_id=" + studentId + " and deal_way = 'dinnerhall'"
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set  totaldinnercosts='" + str(s) + "' where student_id=" + studentId
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        TotalDinnerCostsCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select totaldinnercosts from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set totaldinnercosts='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)