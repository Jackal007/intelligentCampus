from FeatureCalculate import XXCalculater
from Tools import MyLog

class Avg_ChargeCaculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql="select avg_charge from students order by avg_charge"
        self.executer.execute(sql)
        avg_charge = self.executer.fetchall()
        A = avg_charge[int(len(avg_charge) * 0.125)][0]
        B = avg_charge[int(len(avg_charge) * 0.25)][0]
        C = avg_charge[int(len(avg_charge) * 0.375)][0]
        D = avg_charge[int(len(avg_charge) * 0.5)][0]
        E = avg_charge[int(len(avg_charge) * 0.625)][0]
        F = avg_charge[int(len(avg_charge) * 0.75)][0]
        G = avg_charge[int(len(avg_charge) * 0.875)][0]
        H = avg_charge[len(avg_charge) - 1][0]
        self.level = [A, B, C, D, E, F, G]

        
    @MyLog.myException
    def calculate(self):
        '''
        Avg_ChargeCaculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT AVG(deal_cost) FROM card where student_id = "+ studentId+" and deal_type = 'charge'"
        self.executer.execute(sql)
        avg = self.executer.fetchone()[0]
        sql = "update students set avg_charge ='" + str(avg) + "' where student_id=" + studentId
        self.executer.execute(sql)
        
    @MyLog.myException
    def rankit(self):
        '''
        Avg_ChargeCaculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select avg_charge from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set avg_charge='" + s + "' where student_id=" + studentId
        self.executer.execute(sql)