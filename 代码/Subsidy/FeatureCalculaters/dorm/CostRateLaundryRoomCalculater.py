from FeatureCalculate import XXCalculater
from Tools import MyLog

class CostRateLaundryRoomCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_rate_laundryroom from students order by cost_rate_laundryroom"
        self.executer.execute(sql)
        CostAmounts = self.executer.fetchall()
        A = CostAmounts[int(len(CostAmounts) * 0.125)][0]
        B = CostAmounts[int(len(CostAmounts) * 0.25)][0]
        C = CostAmounts[int(len(CostAmounts) * 0.375)][0]
        D = CostAmounts[int(len(CostAmounts) * 0.5)][0]
        E = CostAmounts[int(len(CostAmounts) * 0.625)][0]
        F = CostAmounts[int(len(CostAmounts) * 0.75)][0]
        G = CostAmounts[int(len(CostAmounts) * 0.875)][0]
        H = CostAmounts[len(CostAmounts) - 1][0]
        self.level = [A, B, C, D, E, F, G]
        
    @MyLog.myException
    def calculate(self):
        '''
        CostRateLaundryRoomCalculater.calculate
        '''
        i='LaundryRoom'
        studentId = str(self.student.getStudentId())
        sql = "SELECT\
                    sum(deal_cost)/s\
                FROM\
                    card,\
                    (\
                        SELECT\
                            sum(deal_cost) AS s\
                        FROM\
                            card\
                        WHERE\
                            student_id = " + str(studentId) + "\
                    )as t\
                WHERE\
                    deal_way = '" + i + "'\
                AND student_id = " + str(studentId)
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set cost_rate_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
        self.executer.execute(sql)
                
    @MyLog.myException
    def rankit(self):
        '''
        CostRateLaundryRoomCalculater.rankit
        '''
        i='LaundryRoom'
        studentId = str(self.student.getStudentId())
        sql = "select cost_rate_" + i + " from students where student_id=" + studentId
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set cost_rate_" + i + "='" + str(s) + "' where student_id=" + str(studentId)
        self.executer.execute(sql)