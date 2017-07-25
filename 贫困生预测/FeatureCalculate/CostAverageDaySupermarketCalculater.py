from FeatureCalculate import XXCalculater
from Tools import MyLog

class CostAverageDaySupermarketCalculater(XXCalculater.XXCalculater):
    def setLevel(self):
        sql = "select cost_avg_day_supermarket from students order by cost_avg_day_supermarket"
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
        CostAverageDaySupermarketCalculater.calculate
        '''
        studentId = str(self.student.getStudentId())
        sql = "SELECT\
                    avg(t)\
                FROM\
                    (\
                        SELECT\
                            sum(deal_cost) AS t\
                        FROM\
                            card\
                        WHERE\
                            deal_way = 'Supermarket'\
                        AND student_id = " + str(studentId) + "\
                        GROUP BY\
                            date(deal_date)\
                    )as tt"
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        sql = "update students set cost_avg_day_Supermarket='" + str(s) + "' where student_id=" + str(studentId)
        self.executer.execute(sql)

    @MyLog.myException
    def rankit(self):
        '''
        CostAverageDaySupermarketCalculater.rankit
        '''
        studentId = str(self.student.getStudentId())
        sql = "select cost_avg_day_Supermarket from students where student_id=" + studentId   
        self.executer.execute(sql)
        s = self.executer.fetchone()[0]
        s = self.classify(s)
        sql = "update students_rank set cost_avg_day_Supermarket='" + s + "' where student_id=" + str(studentId) 
        self.executer.execute(sql)
